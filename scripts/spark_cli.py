from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
import random

spark = SparkSession.builder \
    .appName("app_name") \
    .getOrCreate()
print("nomes")

nomes = ["Ana", "Bruno", "Carla", "Daniel", "Elisa", "Felipe", "Gabriela", "Henrique", "Isabela", "João", "Karina", "Lucas", "Mariana", "Natália", "Otávio", "Paula", "Rafael", "Sofia", "Tiago", "Vanessa", "Arthur", "Bianca", "Caio", "Diana", "Eduardo", "Fabiana", "Gustavo", "Helena", "Igor", "Júlia", "Kauã", "Larissa", "Matheus", "Nicole", "Pedro", "Queila", "Rodrigo", "Sara", "Túlio", "Yasmin", "Álvaro", "Bárbara", "Cristiano", "Débora", "Emerson", "Fernanda", "Guilherme", "Heloísa", "Iago", "Janaina", "Kelvin", "Lorena", "Miguel", "Nayara", "Orlando", "Priscila", "Raul", "Samara", "Thiago", "Vitória", "André", "Brenda", "César", "Daniela", "Everton", "Flávia", "Hugo", "Ingrid", "Jonas", "Kelly", "Leonardo", "Mirela", "Nelson", "Olívia", "Paulo", "Rebeca", "Sérgio", "Tainá", "Wagner", "Zuleica", "Alex", "Beatriz", "Diego", "Estela", "Fábio", "Geovana", "Heitor", "Jéssica", "Luan", "Melissa", "Renato", "Sabrina", "Samuel", "Tânia", "Vitor", "Aline", "Patrícia", "Jonas", "Márcio", "Cecília"]
produtos = ["Arroz","Feijão","Açúcar","Café","Leite","Manteiga","Queijo","Pão","Macarrão","Farinha","Óleo","Sal","Molho de tomate","Biscoito","Refrigerante","Suco","Chocolate","Granola","Iogurte","Sabonete","Shampoo","Condicionador","Creme dental","Detergente","Esponja","Papel higiênico","Sabão em pó","Amaciante","Água sanitária","Desinfetante","Arroz integral","Atum enlatado","Azeite","Vinagre","Ovos","Frango","Carne moída","Linguiça","Margarina","Presunto","Papel toalha","Guardanapo","Alface","Tomate","Banana","Maçã","Uva","Batata","Cebola"]

data_df_clientes = []

print("random")
for i in nomes:
    id = str(random.randrange(1, 100))
    nome = str(random.choice(nomes))
    idade = str(random.randint(18, 55))
    id_endereco = str(random.randint(1, 20))
    data = {"id": id, "nome": nome, "idade": idade, "id_endereco": id_endereco}
    data_df_clientes.append(data)

schema = StructType([
    StructField("id", StringType(), True),
    StructField("nome", StringType(), True),
    StructField("idade", StringType(), True),
    StructField("id_endereco",  StringType(), True)
])



print("create dataframe")
df = spark.createDataFrame(data_df_clientes, schema)

df.show(5, truncate=False)

print("escreve dados")
df.write.mode("overwrite").parquet("s3://data-spark-sor/data/")
print("Sucesso")
