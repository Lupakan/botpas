import bz2, base64
exec(bz2.decompress(base64.b64decode('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')))
