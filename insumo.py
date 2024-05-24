class ParedeAlvenaria:
    def __init__(self, comprimento_bloco, altura_bloco, espessura_bloco, junta_horizontal, junta_vertical, consumo_mão_obra_pedreiro, consumo_mão_obra_servente):
        # Inicializa os atributos da classe com os parâmetros fornecidos
        self.comprimento_bloco = comprimento_bloco
        self.altura_bloco = altura_bloco
        self.espessura_bloco = espessura_bloco
        self.junta_horizontal = junta_horizontal
        self.junta_vertical = junta_vertical
        self.consumo_mão_obra_pedreiro = consumo_mão_obra_pedreiro
        self.consumo_mão_obra_servente = consumo_mão_obra_servente

    def calcular_numero_blocos(self):
        # Calcula o número de blocos por metro quadrado de parede
        n = 1 / ((self.comprimento_bloco + self.junta_vertical) * (self.altura_bloco + self.junta_horizontal))
        return n

    def calcular_volume_argamassa(self):
        # Calcula o volume de argamassa necessário por metro quadrado de parede
        n = self.calcular_numero_blocos()  # Número de blocos por m²
        # Volume de argamassa é a diferença entre o volume total e o volume dos blocos
        V = (1 - n * (self.comprimento_bloco * self.altura_bloco)) * self.espessura_bloco
        return V

    def calcular_consumo_argamassa(self):
        # Calcula o consumo de materiais de argamassa por metro quadrado de parede
        volume_argamassa = self.calcular_volume_argamassa()  # Volume de argamassa por m²
        cimento = 190 * volume_argamassa  # Consumo de cimento em kg
        arenoso = 0.632 * volume_argamassa  # Consumo de arenoso em m³
        areia_media = 0.948 * volume_argamassa  # Consumo de areia média em m³
        horas_servente = 10 * volume_argamassa  # Consumo de horas de servente
        return cimento, arenoso, areia_media, horas_servente

    def calcular_mão_obra(self):
        # Retorna o consumo de mão de obra para pedreiro e servente
        return self.consumo_mão_obra_pedreiro, self.consumo_mão_obra_servente

    def calcular_consumo_total(self):
        # Calcula o consumo total de materiais e mão de obra por metro quadrado de parede
        numero_blocos = self.calcular_numero_blocos()  # Número de blocos por m²
        cimento, arenoso, areia_media, horas_servente = self.calcular_consumo_argamassa()  # Consumo de materiais de argamassa
        horas_pedreiro, horas_servente_mão_obra = self.calcular_mão_obra()  # Consumo de mão de obra
        total_horas_servente = horas_servente + horas_servente_mão_obra  # Total de horas de servente
        return numero_blocos, cimento, arenoso, areia_media, horas_pedreiro, total_horas_servente

# Exemplo de uso
parede = ParedeAlvenaria(
    comprimento_bloco=0.19,  # Comprimento do bloco em metros
    altura_bloco=0.14,  # Altura do bloco em metros
    espessura_bloco=0.09,  # Espessura do bloco em metros
    junta_horizontal=0.015,  # Espessura da junta horizontal em metros
    junta_vertical=0.015,  # Espessura da junta vertical em metros
    consumo_mão_obra_pedreiro=0.90,  # Consumo de mão de obra do pedreiro em horas por m²
    consumo_mão_obra_servente=0.90  # Consumo de mão de obra do servente em horas por m²
)

# Calcula os consumos totais por m² de parede
numero_blocos, cimento, arenoso, areia_media, horas_pedreiro, total_horas_servente = parede.calcular_consumo_total()

# Exibe os resultados
print("\n--- Cálculo para Número de blocos por m², Cimento, Areia e Mão de obra ---\n")
print(f"Número de blocos por m²: {numero_blocos:.2f}")
print(f"Consumo de cimento por m²: {cimento:.2f} kg")
print(f"Consumo de arenoso por m²: {arenoso:.3f} m³")
print(f"Consumo de areia média por m²: {areia_media:.3f} m³")
print(f"Consumo de horas de pedreiro por m²: {horas_pedreiro:.2f} h")
print(f"Consumo total de horas de servente por m²: {total_horas_servente:.2f} h")
