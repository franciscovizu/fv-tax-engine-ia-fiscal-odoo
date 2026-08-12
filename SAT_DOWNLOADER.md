# FV® & IA — SAT Downloader

Módulo de descarga masiva de CFDI desde el Web Service del SAT.

## Seguridad

- Nunca subir archivos `.key`, `.cer`, `.pem`, `.pfx` ni contraseñas al repositorio.
- Las credenciales deben permanecer fuera de Git y cargarse únicamente durante la ejecución.
- El módulo debe validar primero certificado y llave antes de intentar autenticación.
- Los XML descargados y paquetes ZIP reales deben almacenarse fuera del repositorio público.

## Flujo previsto

1. Validar e.firma localmente.
2. Autenticar contra el Web Service de descarga masiva del SAT.
3. Crear solicitud de CFDI por rango de fechas y tipo (emitidos/recibidos).
4. Consultar periódicamente el estado de la solicitud.
5. Recuperar paquetes autorizados.
6. Extraer XML en almacenamiento privado.
7. Calcular SHA-256 y UUID para evitar duplicados.
8. Entregar los CFDI al FV Tax Engine y posteriormente a Odoo.

## Estado

La primera fase implementa preparación segura, manifiesto de descargas y deduplicación local. La autenticación productiva se habilitará después de validar el manejo seguro de la e.firma.
