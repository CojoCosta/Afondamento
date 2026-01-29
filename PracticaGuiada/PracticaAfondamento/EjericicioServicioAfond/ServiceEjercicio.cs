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

namespace EjericicioServicioAfond
{
    public partial class ServiceEjercicio : ServiceBase
    {
        public ServiceEjercicio()
        {
            InitializeComponent();
            this.AutoLog = false;
        }
        ServidorEj1Servicios servidor = new ServidorEj1Servicios();
        protected override void OnStart(string[] args)
        {
            Thread lanzarServidor = new Thread(() => { servidor.InitServer(); } );
        }

        protected override void OnStop()
        {
            WriteEvent("Deteniendo el servidor");
        }
        public void WriteEvent(string mensaje)
        {
            EventLog.WriteEntry(mensaje);
        }
    }
}
