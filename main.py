# this is a test file
import multilang

mlang = multilang.multilang()
mlang.set("lang", "tr")


print(mlang.get("merhaba_kullanici") % "canim ben")
mlang.whatIs("dir", True)
mlang.languages(True, True)