import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
