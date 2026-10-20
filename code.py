import pandas as bilu
import matplotlib.pyplot as plt

# 1. Carrega os dados do GitHub
url = "https://raw.githubusercontent.com/AnaoBahiano/bilutomafaleiprimeiro/refs/heads/main/data.csv"
df = bilu.read_csv(url)

# Identifica automaticamente as colunas no seu CSV
col_hora = [c for c in df.columns if any(k in c.lower() for k in ['hora', 'time', 'data', 'timestamp'])][0]
col_temp = [c for c in df.columns if any(k in c.lower() for k in ['temp'])][0]
col_umid = [c for c in df.columns if any(k in c.lower() for k in ['umid', 'hum'])][0]

# Cria uma sequência numérica para cada registro
df['sequencia'] = range(len(df))

# --- GRÁFICO DE BARRAS: TEMPERATURA (Com zoom na altura mínima e máxima) ---
plt.figure(figsize=(14, 6))
plt.bar(df['sequencia'], df[col_temp], color='red', alpha=0.85, width=0.6)

# Configura o eixo X com as horas reais
plt.xticks(df['sequencia'], df[col_hora], rotation=90)

# Dá o zoom vertical exato entre o menor e o maior valor (com uma leve margem de respiro)
min_temp = df[col_temp].min()
max_temp = df[col_temp].max()
plt.ylim(min_temp - 0.2, max_temp + 0.2)

plt.title('Variação da Temperatura por Registro', fontsize=14, fontweight='bold')
plt.xlabel('Hora / Momento', fontsize=12)
plt.ylabel('Temperatura (°C)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# --- GRÁFICO DE BARRAS: UMIDADE (Com zoom na altura mínima e máxima) ---
plt.figure(figsize=(14, 6))
plt.bar(df['sequencia'], df[col_umid], color='blue', alpha=0.85, width=0.6)

plt.xticks(df['sequencia'], df[col_hora], rotation=90)

# Dá o zoom vertical exato para a umidade
min_umid = df[col_umid].min()
max_umid = df[col_umid].max()
plt.ylim(min_umid - 1.0, max_umid + 1.0)

plt.title('Variação da Umidade por Registro', fontsize=14, fontweight='bold')
plt.xlabel('Hora / Momento', fontsize=12)
plt.ylabel('Umidade (%)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
