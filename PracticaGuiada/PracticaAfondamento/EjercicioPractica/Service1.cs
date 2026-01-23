using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Linq;
using System.ServiceProcess;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace EjercicioPractica
{
    public partial class MiPrimerServicio : ServiceBase
    {
        // Constructor donde se inicializan algunas propiedades de interés
        public MiPrimerServicio()
        {
            InitializeComponent();
        }
        public void WriteEvent(string mensaje)
        {
            // Nombre de la fuente de eventos.
            const string nombre = "MiPrimerServicio";

            // Escribe el mensaje deseado en el visor de eventos
            EventLog.WriteEntry(nombre, mensaje);
        }

        private System.Timers.Timer timer;
        //Se ejecuta cuando inicia el servicio
        protected override void OnStart(string[] args)
        {
            WriteEvent("Iniciando MiPrimerServicio mediante OnStart");
            timer = new System.Timers.Timer();
            timer.Interval = 10000; // cada 10 segundos
            timer.Elapsed += this.TimerTick;
            timer.Start();
        }
        private int t = 0;
        public void TimerTick(object sender, System.Timers.ElapsedEventArgs args)
        {
            WriteEvent($"MiPrimerServicio lleva ejecutándose {t} segundos.");
            t += 10;
        }

        //Se ejecuta cuando pausa el servicio
        protected override void OnPause()
        {
            WriteEvent("MiPrimerServicio en Pausa");
            timer.Stop();
        }

        //Se ejecuta cuando para el servicio
        protected override void OnStop()
        {
            WriteEvent("Deteniendo MiPrimerServicio");
            timer.Stop();
            timer.Dispose();
            t = 0;
        }
        //Se ejecuta cuando continua tras la pausa el servicio
        protected override void OnContinue()
        {
            WriteEvent("Continuando MiPrimerServicio");
            timer.Start();
        }
        static void Main()
        {
            ServiceBase[] ServicesToRun;
            ServicesToRun = new ServiceBase[]
            {
                new MiPrimerServicio()
            };
            ServiceBase.Run(ServicesToRun);
        }
//        sc create "MiPrimerServicio" binPath="C:\Users\alumnoinfo\source\repos\Afondamento\PracticaGuiada\PracticaAfondamento\EjercicioPractica\bin\Debug\MiPrimerServicio.exe"
//DisplayName="Mi Primer Servicio" start=demand

    }
}