# multilangPY


### Import the library
```python
from multilang import multilang
```

## Using

####  > How to starting
```python
mlang = multilang()
```

#### > Set Languages Directory
```python
mlang.set("dir", "../demo/langs/")
```

#### > whatIs function
```python
mlang.whatIs(value, print4me=False)
```
| value | what is does | ouput |
|--|--|--|
| lang or language | Prints the selected language | return
| dir or directory | Prints the selected directory | return


#### > List the language in the defined direcory
```python 
mlang.languages(print4me=False, helper=False)
```

| paramters | what is does | output |
|-------------|--------------|--------|
| print4me | Print for you language file(s) in directory | array |
| helper | writes in detail the file(s) in directory. You just using with print4me. | just try :) |


#### > How to create the language file (json)
For example, the folder with the language files: `../multilang/languages/` and we create a language folder in the directory. Create `LANGUAGE.json`  for example `ru.json` and  `az.json`
`"CALL_NAME": "TEXT or WORD"`
```json
// ru.json
{
	"merhaba": "Привет",
	"merhaba_kullanici": "Привет %s"
}

// az.json
{
	"merhaba": "Salamlar",
	"merhaba_kullanici": "Salam %s"
}
```

#### > How to get the text or word
```python
mlang.get(CALLED NAME)
```

## Example Using
```python
# main.py
import multilang

mlang = multilang.multilang()
mlang.set("dir", "app/langs/") # Set the new directory
mlang.set("lang", "az") # Set az lang 

mlang.get("merhaba") # Output (return): Salamlar
print(mlang.get("merhaba_kullanici") % "Melih") # Output (print): Salam Melih
```
