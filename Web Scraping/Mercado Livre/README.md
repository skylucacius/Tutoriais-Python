# Web Scraping do site do Mercado Livre (ML) para 10.000 produtos !

## Para efetuar este scraping, basta abrir o console e:

1. executar um "pip install -r requisitos.txt";

2. executar "scrapy crawl ml -o resultado.json" no diretório "mercadolivre".

O resultado é um arquivo JSON contendo dados dos produtos da oferta do dia do do mercado livre. a variável "AUTOTHROTTLE_ENABLE" foi setada para true, para evitar um possível banimento pelo site do ML. Essa aplicação é o resultado do tutorial disponível em: https://www.youtube.com/watch?v=7le4AGwtH94&t=146s 
[do canal Programação na Prática]