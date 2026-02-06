[![Docker Pulls](https://img.shields.io/docker/pulls/aapovaari/password-generator)](https://hub.docker.com/r/aapovaari/password-generator)

# Salasanageneraattori

## Ominaisuudet
- Käyttää `secrets`-kirjastoa aidon satunnaisuuden takaamiseksi.
- Varmistaa, että salasanassa on aina vähintään yksi pieni kirjain, iso kirjain, numero ja erikoismerkki.
- Syötteen validointi virheiden estämiseksi.

## Miten käytetään
1. Varmista, että Python 3 on asennettuna.
2. Aja komento
```bash
python main.py
```
3. Syötä haluttu pituus (min. 4).

## Teknologiat
- Python 3.x
- Moduulit: `secrets`, `string`
 