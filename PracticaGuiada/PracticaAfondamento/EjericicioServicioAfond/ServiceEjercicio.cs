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
using System.Timers;

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
        protected override void OnStart(string[] args)
        {
            servidor = new ServidorEj1Servicios();
            Thread lanzarServidor = new Thread(servidor.InitServer);
            lanzarServidor.Start();
        }

        protected override void OnStop()
        {
            servidor.ServerRunning = false;
            WriteEvent("Deteniendo el servidor");
        }
        public void WriteEvent(string mensaje)
        {
            EventLog.WriteEntry(mensaje);
        }
    }
    //sc create "ServiceEjercicio" binPath= \""C:\Users\Diego Costa\Desktop\Afondamento\PracticaGuiada\PracticaAfondamento\EjericicioServicioAfond\bin\Debug\EjericicioServicioAfond.exe\"" DisplayName="AAAEjercicioAfondamento" start=demand
    //TODO hacer este comando -> sc description MiPrimerServicio "Servicio de prueba"
}
