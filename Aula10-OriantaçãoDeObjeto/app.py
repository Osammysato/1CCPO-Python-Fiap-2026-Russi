from aluno import Aluno
from disciplina import Disciplina

# criar / instanciar 1 aluno
aluno1 = Aluno("João", "123456", "Ciências da Computação")

# criar / instanciar 2 disciplinas
sers = Disciplina("Soluções Renováveis", "Tritiack")
cs = Disciplina("Computer Science", "Lucas")

# DESCOMENTADO: matricular o aluno nas disciplinas primeiro
aluno1.matricular(sers)
aluno1.matricular(cs)

# AGORA VAI FUNCIONAR: adicionar nota do aluno referente às disciplinas
aluno1.adicionar_nota(sers, 10)
aluno1.adicionar_nota(sers, 7)
aluno1.adicionar_nota(cs, 8.9)
aluno1.adicionar_nota(cs, 7.6)

print(aluno1.notas_por_disciplina(cs))
print(aluno1.calcular_media_g())