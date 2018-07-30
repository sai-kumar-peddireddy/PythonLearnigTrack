"""
Sun Jul 29 05:58:28 IST 2018
source : https://www.geeksforgeeks.org/byte-objects-vs-string-python/


 encode(...)
 |      S.encode(encoding='utf-8', errors='strict') -> bytes
 |
 |      Encode S using the codec registered for encoding. Default encoding
 |      is 'utf-8'. errors may be given to set a different error
 |      handling scheme. Default is 'strict' meaning that encoding errors raise
 |      a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
 |      'xmlcharrefreplace' as well as any other name registered with
 |      codecs.register_error that can handle UnicodeEncodeErrors.



"""
name = "sai kumar"

byteobj = b"sai kumar"  # byte obj

encodedval = name.encode("ASCII")

if byteobj == encodedval:
    print("encoded value and byte obj are asme")
else:
    print("encoded value and byte obj not are asme")


decodeval = byteobj.decode("ASCII")

if name == decodeval:
    print("decod value and string  are asme")
else:
    print("decod value and string are not asme")

