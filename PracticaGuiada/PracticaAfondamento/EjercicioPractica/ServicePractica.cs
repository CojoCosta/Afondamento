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

namespace MiPrimerServicio
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
            const string nombre = "MiPrimerServicio"; // Nombre de la fuente de eventos.
                                                      // Escribe el mensaje deseado en el visor de eventos
            EventLog.WriteEntry(nombre, mensaje);

        }

        private System.Timers.Timer timer;
        protected override void OnStart(string[] args)
        {
            WriteEvent("Iniciando MiPrimerServicio mediante OnStart");
            timer = new System.Timers.Timer();
            timer.Interval = 10000;
            timer.Elapsed += this.TimerTick;
            timer.Start();

        }
        private int t = 0;
        public void TimerTick(object sender, System.Timers.ElapsedEventArgs args)
        {

            WriteEvent($"MiPrimerServicio lleva ejecutándose {t} segundos");
            t += 10;
        }

        protected override void OnPause()
        {
            WriteEvent("MiPrimerServicio en Pausa");
            timer.Stop();
        }
        protected override void OnContinue()
        {
            WriteEvent("Continuando MiPrimerServicio");
            timer.Start();
        }
        protected override void OnStop()
        {
            WriteEvent("Deteniendo MiPrimerServicio");
            timer.Stop();
            timer.Dispose();
            t = 0;
        }

        //sc create "MiPrimerServicio" binPath="C:\Users\Diego Costa\Desktop\Afondamento\PracticaGuiada\PracticaAfondamento\EjercicioPractica\bin\Release\MiPrimerServicio.exe" DisplayName="Mi Primer Servicio" start=demand
        //sc create "MiPrimerServicio" binPath="C:\Users\Diego Costa\Desktop\Afondamento\PracticaGuiada\PracticaAfondamento\EjercicioPractica\bin\Release\EjercicioPractica.exe" DisplayName="Mi Primer Servicio" 
    }
}