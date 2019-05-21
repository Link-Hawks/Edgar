from psutil import pids, Process


class ValidacaoHelper:

    @staticmethod
    def rodando(nome_servico):
        lista_processos_rodando = pids()
        rodando = False
        for processo_pid in lista_processos_rodando:
            processo = Process(processo_pid)
            if processo.name == nome_servico:
                return rodando
        return rodando
