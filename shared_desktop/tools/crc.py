import zlib

file_path = "C:/rag901.t"

with open(file_path, "rb") as file:
    data = file.read()
    crc32_value = zlib.crc32(data) & 0xFFFFFFFF  # Получаем CRC32 и маскируем его

print(f"Контрольная сумма CRC файла {file_path}: {crc32_value}")