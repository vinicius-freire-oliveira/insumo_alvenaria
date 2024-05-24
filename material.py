# Definindo os consumos por m² de parede
consumo_cimento_por_m2 = 2.79  # kg/m²
consumo_arenoso_por_m2 = 0.0093  # m³/m²
consumo_areia_por_m2 = 0.0139  # m³/m²
consumo_blocos_por_m2 = 31.47  # un/m²

# Estoque disponível
estoque_cimento_sacos = 12
estoque_arenoso_m3 = 3
estoque_areia_m3 = 5
estoque_blocos = 10000

# Convertendo o estoque de cimento para kg (cada saco tem 50 kg)
estoque_cimento_kg = estoque_cimento_sacos * 50

# Calculando a área máxima que pode ser construída com cada material
area_max_cimento = estoque_cimento_kg / consumo_cimento_por_m2
area_max_arenoso = estoque_arenoso_m3 / consumo_arenoso_por_m2
area_max_areia = estoque_areia_m3 / consumo_areia_por_m2
area_max_blocos = estoque_blocos / consumo_blocos_por_m2

# Determinando a área mínima que pode ser construída com os materiais disponíveis
area_maxima_construivel = min(area_max_cimento, area_max_arenoso, area_max_areia, area_max_blocos)

# Exibindo os resultados
print(f"Área máxima que pode ser construída com o cimento disponível: {area_max_cimento:.2f} m²")
print(f"Área máxima que pode ser construída com o arenoso disponível: {area_max_arenoso:.2f} m²")
print(f"Área máxima que pode ser construída com a areia disponível: {area_max_areia:.2f} m²")
print(f"Área máxima que pode ser construída com os blocos disponíveis: {area_max_blocos:.2f} m²")
print(f"Área máxima de alvenaria que pode ser construída sem compra adicional de material: {area_maxima_construivel:.2f} m²")
