from disciplina import Disciplina

class Aluno:
    def __init__(self, nome, rm, curso):
        self.nome = nome
        self.rm = rm
        self.curso = curso
        self.disciplinas = []           #[Disciplina, Disciplina]
        self.nt_dscpln = {}             #{"Modelagem...": [nota, nota...]}

    def matricular(self, disciplina: Disciplina):
        self.disciplinas.append(disciplina)
        self.nt_dscpln.setdefault(disciplina.nome, [])

    def adicionar_nota(self, disciplina: Disciplina, nota: float):
        self.nt_dscpln[disciplina.nome].append(nota)

    def media_d(self, d: Disciplina) -> float:
        notas = self.nt_dscpln.get(d.nome, [])
        return sum(notas) / len(notas)

    def media_g(self) -> float:
        medias = []
        for d in self.disciplinas:
            media_d = self.media_d(d)
            medias.append(media_d)
        return sum(medias / len(medias))