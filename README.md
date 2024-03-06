# Brother-SNMP

## Descrição
Projeto para consulta de recursos em impressoras Brother utilizando o protocolo SNMP. 

## Impressoras Compatíveis

- Brother DCP-L5652DN
- Brother DCP 8157DN
- Brother DCP 8152DN
- Brother MFC-J6935DW
- Brother MFC L6702DW
- Brother MFC 7460DN
- Brother MFC 9460CW
- Brother HL_l2360DW
- Brother 5350DN
- Brother L2540

## Como obter o nível dos recursos
As informações específicas, como os níveis de toner e cilindro, são armazenadas em um OID chamado "brInfoMaintenance" (.1.3.6.1.4.1.2435.2.3.9.4.2.1.5.5.8.0). As informações estão em formato hexadecimal, e cada coluna de 7 grupos de 2 caracteres (por exemplo: 31 01 04 00 00 00 64) corresponde a um recurso diferente. Os dois primeiros dígitos representam o tipo de recurso, como mostra a tabela abaixo, enquanto os dois últimos representam o valor do recurso.

## Tabela de Valores
Existe uma tabela dos valores conhecidos dos dois primeiros dígitos do código hexadecimal:

- "11": VAL_DRUM_COUNT
- "31": VAL_BLACK_TONER_STATUS
- "32": VAL_CYAN_TONER_STATUS
- "33": VAL_MAGENTA_TONER_STATUS
- "34": VAL_YELLOW_TONER_STATUS
- "41": VAL_DRUM_REMAIN
- "63": VAL_DRUM_STATUS
- "69": VAL_BELT_REMAIN
- "6a": VAL_FUSER_REMAIN
- "6b": VAL_LASER_REMAIN
- "6c": VAL_PF_MP_REMAIN
- "6d": VAL_PF_1_REMAIN
- "6f": VAL_BLACK_TONER_REMAIN
- "70": VAL_CYAN_TONER_REMAIN
- "71": VAL_MAGENTA_TONER_REMAIN
- "72": VAL_YELLOW_TONER_REMAIN
- "73": VAL_CYAN_DRUM_COUNT
- "74": VAL_MAGENTA_DRUM_COUNT
- "75": VAL_YELLOW_DRUM_COUNT
- "7e": VAL_BLACK_DRUM_COUNT
- "79": VAL_CYAN_DRUM_REMAIN
- "7a": VAL_MAGENTA_DRUM_REMAIN
- "7b": VAL_YELLOW_DRUM_REMAIN
- "80": VAL_BLACK_DRUM_REMAIN
- "81": VAL_BLACK_TONER
- "82": VAL_CYAN_TONER
- "83": VAL_MAGENTA_TONER
- "84": VAL_YELLOW_TONER
- "a1": VAL_BLACK_TONER_REMAIN
- "a2": VAL_CYAN_TONER_REMAIN
- "a3": VAL_MAGENTA_TONER_REMAIN
- "a4": VAL_YELLOW_TONER_REMAIN

## Processo de Extração
Para obter o nível dos recursos, é necessário separar o código hexadecimal em partes de cada informação (em grupos de 7). Remover os numeros padrão "01 04" seguintes e capturar os últimos 4 grupos de dados. Esses grupos devem ser convertidos para decimal, resultando no valor desejado do recurso. Essa é provavelmente a parte mais complexa do projeto.
