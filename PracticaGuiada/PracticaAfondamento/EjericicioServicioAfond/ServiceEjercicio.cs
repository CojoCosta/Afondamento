using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Linq;
using System.Net;
using System.ServiceProcess;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Timers;
//TODO INSTRUCCIONES DE USO:
//ENTRA EN MI SESION (DIEGO COSTA) PARA CORREGIRLO, EN ALUMNOINFO ME DA ERRORES AL INICIAR EL PROGRAMA 
namespace EjericicioServicioAfond
{
    public partial class ServiceEjercicio : ServiceBase
    {
        public ServiceEjercicio()
        {
            InitializeComponent();
            this.AutoLog = false;
        }
        ServidorEj1Servicios servidor;
        /// <summary>
        /// Inicia el servicio lanzando un hilo con la funcion InitServer de la clase ServidorEj1Servicios
        /// </summary>
        /// <param name="args"></param>
        protected override void OnStart(string[] args)
        {
            servidor = new ServidorEj1Servicios();
            Thread lanzarServidor = new Thread(servidor.InitServer);
            lanzarServidor.Start();
        }

        /// <summary>
        /// Detiene el funcionamiento del servicio
        /// </summary>
        protected override void OnStop()
        {
            servidor.ServerRunning = false;
            WriteEvent("Deteniendo el servidor");
        }

        /// <summary>
        /// Escribe en el visor de eventos el string pasado como parametro
        /// </summary>
        /// <param name="mensaje">string informativo que será en el visor de eventos</param>
        public void WriteEvent(string mensaje)
        {
            const string nombreServicio = "ServiceEjercicio";
            try
            {
                EventLog.WriteEntry(nombreServicio, mensaje);
            }
            catch (Exception ex) 
            {
                EventLog.WriteEntry("FUNCIONA");
                servidor.escribirComandos($"[ERROR] {nombreServicio} erróneo", IPAddress.Any ,0);
            }
        }
    }
    //sc create "ServiceEjercicio" binPath= \""C:\Users\Diego Costa\Desktop\Afondamento\PracticaGuiada\PracticaAfondamento\EjericicioServicioAfond\bin\Release\EjericicioServicioAfond.exe\"" DisplayName="AAAEjercicioAfondamento" start=demand

    //sc description ServiceEjercicio "Proporciona datos temporales de fecha(date) y hora(time), por separado o en un solo comando(all)."
}
