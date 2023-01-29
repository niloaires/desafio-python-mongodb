from django_cron import CronJobBase, Schedule




class MyCronJob(CronJobBase):
    run_min=2
    repetir_em_caso_erro=5
    schedule=Schedule(run_every_mins=run_min, retry_after_failure_mins=repetir_em_caso_erro)
    code='api.checar_status'
    def do(self):
        pass