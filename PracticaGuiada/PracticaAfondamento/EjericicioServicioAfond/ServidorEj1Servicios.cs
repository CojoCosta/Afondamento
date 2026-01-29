using System;
using System.Collections.Generic;
using System.Data;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Net;
using System.Net.Sockets;
using System.ServiceProcess;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace EjericicioServicioAfond
{
    internal class ServidorEj1Servicios
    {
        public bool ServerRunning { set; get; } = true;
        Socket s;
        ServiceEjercicio service = new ServiceEjercicio();
        //CONSTANTES
        int defaultPort = 31416;
        string comandoNoValido = "Comando no válido: ";
        string errorPuerto = "Leer archivo inexistente o puerto no válido\nPuerto por defecto: ";
        string puertoOcupado = "Puerto en uso, servidor cerrado";
        public void InitServer()
        {
            using (s = new Socket(AddressFamily.InterNetwork, SocketType.Stream, ProtocolType.Tcp))
            {
                try
                {
                    IPEndPoint ie = new IPEndPoint(IPAddress.Any, PuertoEnEscucha("puerto"));
                    s.Bind(ie);
                    s.Listen(10);
                    Console.WriteLine($"Servidor iniciado. " + $"Escuchando en {ie.Address}:{ie.Port}");
                    Console.WriteLine("Esperando conexiones... (Ctrl+C para salir)");
                    while (ServerRunning)
                    {
                        Socket cliente = s.Accept();
                        Thread hilo = new Thread(() => ProtocoloCliente(cliente));
                        hilo.IsBackground = true;
                        hilo.Start();
                    }
                }
                catch (SocketException e)
                {
                    service.WriteEvent($"{puertoOcupado}");
                    escribirErrores($"{puertoOcupado}");
                    s.Close();
                }
            }
        }

        public void ProtocoloCliente(Socket sCliente)
        {
            using (sCliente)
            {
                IPEndPoint ieCliente = (IPEndPoint)sCliente.RemoteEndPoint;
                Console.WriteLine($"Cliente conectado:{ieCliente.Address} " + $"en puerto {ieCliente.Port}");
                Encoding codificacion = Console.OutputEncoding;
                using (NetworkStream ns = new NetworkStream(sCliente))
                using (StreamReader sr = new StreamReader(ns))
                using (StreamWriter sw = new StreamWriter(ns))
                {
                    sw.AutoFlush = true;
                    string msg = "";
                    DateTime fechaYHora;
                    try
                    {
                        msg = sr.ReadLine();
                        if (msg != null)
                        {
                            switch (msg.Trim())
                            {
                                case "time":
                                    fechaYHora = DateTime.Now;
                                    sw.WriteLine(fechaYHora.ToString("HH:mm:ss"));
                                    break;
                                case "date":
                                    fechaYHora = DateTime.Now;
                                    sw.WriteLine(fechaYHora.ToString("dd/MM/yyyy"));
                                    break;
                                case "all":
                                    fechaYHora = DateTime.Now;
                                    sw.WriteLine(fechaYHora.ToString("dd/MM/yyyy -- HH:mm:ss"));
                                    break;
                                default:
                                    service.WriteEvent($"{comandoNoValido}{msg}");
                                    escribirErrores($"{comandoNoValido}{msg}");
                                    break;
                            }
                            Console.WriteLine($"El cliente escribió: {msg}");
                        }
                    }
                    catch (Exception ex) when (ex is IOException || ex is SocketException)
                    {
                        msg = null;
                    }
                    Console.WriteLine("Cliente desconectado.\nConexión cerrada");
                }
            }
        }

        string programdata = Environment.GetEnvironmentVariable("Programdata");
        int puertoEscucha = 0;
        public int PuertoEnEscucha(string fileName)
        {
            try
            {
                DirectoryInfo dir = new DirectoryInfo(programdata);
                string path = $"{programdata}\\{fileName}.txt";
                using (StreamReader sr = new StreamReader(path))
                {
                    puertoEscucha = int.Parse(sr.ReadToEnd());
                    return puertoEscucha;
                }
            }
            catch (Exception ex) when (ex is FileNotFoundException || ex is IOException || ex is UnauthorizedAccessException)
            {
                service.WriteEvent($"{errorPuerto}{defaultPort}");
                escribirErrores($"{errorPuerto}{defaultPort}");
                return defaultPort;
            }
        }

        public void escribirErrores(string mensaje)
        {
            try
            {
                DateTime timeStamp = DateTime.Now;
                DirectoryInfo dir = new DirectoryInfo(programdata);
                string path = $"{programdata}\\errores.txt";
                using (StreamWriter sw = new StreamWriter(path))
                {
                    sw.WriteLine($"[ERROR] {mensaje} - {timeStamp.ToString("dd/MM/yyyy -- HH:mm:ss")}");
                }
            }
            catch (Exception e)
            {
                service.WriteEvent("Archivo inexistente o erróneo");
            }
        }
       
    }
}
