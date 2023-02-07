# Aqui vamos a ir documentando cosas para acceder a la api

Primero necesito acceder a un link que tengo que crear

Accedemos a esta url para una ventana de autorizacion

https://api.instagram.com/oauth/authorize
  ?client_id=718122439898547
  &redirect_uri=https://github.com/LuckyCaves/Aprendiendo-Programar
  &scope=user_profile,user_media, instagram_graph_user_profile
  &response_type=code

La ventana de autorizacion me regresó esta url

https://github.com/LuckyCaves/Aprendiendo-Programar?code=AQDs7g4KQzmz5Iqf5Dt2FrAC2EYeEcaMl__NeegETDhFLldACyvV9c7PMWOZUyXDDnI9fptoceddaebSLt9UyLC2tqcQMaX_FQqv9t50HvfBYmDfUhRNmg2cKdTUJJhIl4yxJSlyWD2eV-2j6u4gIy9-wuCew_Z5HtW5PUCsQ2QiQikAoU4uttBmC-tlr2Zke9PbP1-6ckmDZmUgfDggpeGn9638BGEtchBLRXerM5ZFtA

debo de unicamente tomar la parte despues de code

AQDs7g4KQzmz5Iqf5Dt2FrAC2EYeEcaMl__NeegETDhFLldACyvV9c7PMWOZUyXDDnI9fptoceddaebSLt9UyLC2tqcQMaX_FQqv9t50HvfBYmDfUhRNmg2cKdTUJJhIl4yxJSlyWD2eV-2j6u4gIy9-wuCew_Z5HtW5PUCsQ2QiQikAoU4uttBmC-tlr2Zke9PbP1-6ckmDZmUgfDggpeGn9638BGEtchBLRXerM5ZFtA

Ahora vamos a cambiar el código por un token

curl -X POST https://api.instagram.com/oauth/access_token 
\ -F client_id=718122439898547 
\ -F client_secret=f91f66fddf401f5360e91293244e514c 
\ -F grant_type=authorization_code 
\ -F redirect_uri=https://github.com/LuckyCaves/Aprendiendo-Programar 
\ -F code=AQDs7g4KQzmz5Iqf5Dt2FrAC2EYeEcaMl__NeegETDhFLldACyvV9c7PMWOZUyXDDnI9fptoceddaebSLt9UyLC2tqcQMaX_FQqv9t50HvfBYmDfUhRNmg2cKdTUJJhIl4yxJSlyWD2eV-2j6u4gIy9-wuCew_Z5HtW5PUCsQ2QiQikAoU4uttBmC-tlr2Zke9PbP1-6ckmDZmUgfDggpeGn9638BGEtchBLRXerM5ZFtA


{"access_token": "IGQVJVN0FqZAzFHOHlEbUJsNkhJVXNERURwZAWhvU3Mtd29SeTl0LVJheDBqRVNydVdEWF9uNzQ5NkZAOeU5rRVJDdk82bWljWUhfdUkxdU1KUzVNTGlzSFNjZA0NJVVVIWE5vV0wwd21DVVNad0VITVRWa0hsS0NqbS0zX3VF", "user_id": 17841405764308284}

Este es nuestro acces token y nuestro id de usuario

Primero intentaremos usar la api para revisar que nuestro id de usuario sea el mismo y que nuestro nombre de usuario sea el correcto 

curl -X GET 'https://graph.instagram.com/me?fields=id,username&access_token=IGQVJVN0FqZAzFHOHlEbUJsNkhJVXNERURwZAWhvU3Mtd29SeTl0LVJheDBqRVNydVdEWF9uNzQ5NkZAOeU5rRVJDdk82bWljWUhfdUkxdU1KUzVNTGlzSFNjZA0NJVVVIWE5vV0wwd21DVVNad0VITVRWa0hsS0NqbS0zX3VF

funcionó, me regresó el usuario completo y mi identificador asumiré que es el mismo

Ahora vamos a crear la función para detectar mis seguidores y contrastarlo con mis seguidos

Obtuve el error de que no se podía hacer, vamos a cambiar los permisos

https://api.instagram.com/oauth/authorize
  ?client_id=718122439898547
  &redirect_uri=https://github.com/LuckyCaves/Aprendiendo-Programar
  &redirect_uri=https://github.com/LuckyCaves/Aprendiendo-Programar
  &scope=user_profile,user_media, instagram_graph_user_profile
  &response_type=code


https://api.instagram.com/oauth/authorize?grant_type=ig_exchange_token&client_secret=f91f66fddf401f5360e91293244e514c&access_token=IGQVJVN0FqZAzFHOHlEbUJsNkhJVXNERURwZAWhvU3Mtd29SeTl0LVJheDBqRVNydVdEWF9uNzQ5NkZAOeU5rRVJDdk82bWljWUhfdUkxdU1KUzVNTGlzSFNjZA0NJVVVIWE5vV0wwd21DVVNad0VITVRWa0hsS0NqbS0zX3VF

## Primer intento salió mal, un segundo intento

https://api.instagram.com/oauth/authorize
  ?client_id=736535307795779
  &redirect_uri=https://github.com/LuckyCaves/Aprendiendo-Programar
  &scope=user_profile,user_media
  &response_type=code

# Estoy cansado, termino por hoy