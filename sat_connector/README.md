# FV® SAT Descarga Masiva Connector

Módulo en desarrollo para automatizar la recuperación de CFDI emitidos y recibidos mediante el Web Service de Descarga Masiva del SAT.

## Objetivo de la primera versión

1. Autenticarse con e.firma.
2. Solicitar CFDI por rango de fechas.
3. Verificar el estado de cada solicitud.
4. Descargar los paquetes autorizados por el SAT.
5. Descomprimir XML.
6. Evitar duplicados por UUID.
7. Guardar un cursor de sincronización para continuar desde el último punto exitoso.
8. Ejecutar sincronización diaria y recuperación histórica sin intervención manual.

## Seguridad

Nunca se deben versionar credenciales reales. El repositorio ya ignora `.env`; adicionalmente, los archivos `.cer`, `.key`, paquetes descargados y XML reales deben permanecer fuera de Git.

Variables previstas:

```text
SAT_RFC=XXXXXXXXXXXXX
SAT_CER_PATH=/ruta/segura/efirma.cer
SAT_KEY_PATH=/ruta/segura/efirma.key
```

La contraseña de la llave privada no se guardará en código fuente. En la etapa de prueba se inyectará mediante un secreto local/variable de entorno segura.

## Estado actual

La rama `feature/sat-descarga-masiva` contiene la estructura inicial de configuración y persistencia del estado incremental. El siguiente bloque es implementar la firma/autenticación WS-Security y los clientes SOAP de solicitud, verificación y descarga.
