import hashlib, zlib

async def mysql1323(x):
    from passlib.hash import mysql323
    return mysql323.encrypt(x)

async def mysql141(x):
    from passlib.hash import mysql41
    return mysql41.encrypt(x)

async def mssql2000(x):
    from passlib.hash import mssql2000 as m20
    return m20.encrypt(x)

async def mssql2005(x):
    from passlib.hash import mssql2005 as m25
    return m25.encrypt(x)

async def md4(x):
    m = hashlib.new("md4")
    m.update(x)
    return m.hexdigest()

async def md5(x):
    m = hashlib.new("md5")
    m.update(x)
    return m.hexdigest()

async def sha1(x):
    m = hashlib.new("sha1")
    m.update(x)
    return m.hexdigest()

async def Sha224(x):
    m = hashlib.new("sha224")
    m.update(x)
    return m.hexdigest()

async def Sha256(x):
    m = hashlib.new("sha256")
    m.update(x)
    return m.hexdigest()

async def Sha384(x):
    m = hashlib.new("sha384")
    m.update(x)
    return m.hexdigest()

async def Sha512(x):
    m = hashlib.new("sha512")
    m.update(x)
    return m.hexdigest()

async def Ripemd160(x):
    m = hashlib.new("ripemd160")
    m.update(x)
    return m.hexdigest()

async def Whirlpool(x):
    m = hashlib.new("whirlpool")
    m.update(x)
    return m.hexdigest()

async def crc32(x):
    h = zlib.crc32(x)
    return ('%08X' % (h & 0xffffffff,)).lower()

async def adler32(x):
    h = zlib.adler32(x)
    return ('%08X' % (h & 0xffffffff,)).lower()

async def des(x):
    from passlib.hash import des_crypt
    return des_crypt.encrypt(x)

async def Bsdi_Crypt(x):
    from passlib.hash import bsdi_crypt
    return bsdi_crypt.encrypt(x)

async def Bigcrypt(x):
    from passlib.hash import bigcrypt
    return bigcrypt.encrypt(x)

async def Crypt16(x):
    from passlib.hash import crypt16
    return crypt16.encrypt(x)

async def Md5_crypt(x):
    from passlib.hash import md5_crypt as mc
    return mc.encrypt(x)

async def Sha1_crypt(x):
    from passlib.hash import sha1_crypt as mc
    return mc.encrypt(x)

async def Sha256_crypt(x):
    from passlib.hash import sha256_crypt as mc
    return mc.encrypt(x)

async def Sha512_crypt(x):
    from passlib.hash import sha512_crypt as mc
    return mc.encrypt(x)

async def Sun_md5(x):
    from passlib.hash import sun_md5_crypt as mc
    return mc.encrypt(x)

async def apache_md5(x):
    from passlib.hash import apr_md5_crypt as mc
    return mc.encrypt(x)

async def phppass(x):
    from passlib.hash import phpass as mc
    return mc.encrypt(x)

async def Cryptaculars_PBDF2(x):
    from passlib.hash import cta_pbkdf2_sha1 as mc
    return mc.encrypt(x)

async def Dwine_PBDF2(x):
    from passlib.hash import dlitz_pbkdf2_sha1 as mc
    return mc.encrypt(x)

async def Atlassians_PBKDF2(x):
    from passlib.hash import cta_pbkdf2_sha1 as mc
    return mc.encrypt(x)

async def Django_sha1(x):
    from passlib.hash import django_pbkdf2_sha1 as m25
    return m25.encrypt(x)

async def django_sha256(x):
    from passlib.hash import django_pbkdf2_sha256 as m25
    return m25.encrypt(x)

async def grup_pbkdf2(x):
    from passlib.hash import grub_pbkdf2_sha512 as m25
    return m25.encrypt(x)

async def SCRAM(x):
    from passlib.hash import scram as mc
    return mc.encrypt(x)

async def FreeBSD_nthash(x):
    from passlib.hash import bsd_nthash as mc
    return mc.encrypt(x)

async def oracle11(x):
    from passlib.hash import oracle11 as m25
    return m25.encrypt(x)

async def lanManager(x):
    from passlib.hash import lmhash as m25
    return m25.encrypt(x)

async def nthash(x):
    from passlib.hash import nthash as m25
    return m25.encrypt(x)

async def cisco_type_7(x):
    from passlib.hash import cisco_type7 as m25
    return m25.encrypt(x)

async def fhsp(x):
    from passlib.hash import fshp as m25
    return m25.encrypt(x)