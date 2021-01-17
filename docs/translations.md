# Translations

## RaspAP in your language
Owing to its utility and low cost, the Raspberry Pi's reach extends to all corners of the globe. As our way of honoring this, we've made an effort to support internationalization (often abbreviated **i18n**) with RaspAP. Given the response from [this issue](https://github.com/billz/raspap-webgui/issues/121) it became obvious that translations are something that the community both wanted and were willing to contribute to.

On Linux systems, [GNU's Gettext](https://www.gnu.org/software/gettext/) provides a standardized way of managing multi-lingual messages. In order for Gettext to work with different languages, you must configure a language package on your RPi corresponding to one of our supported translations.

To list languages currently installed on your system, use `locale -a` at the shell prompt. On a fresh install of Raspbian, this should return a list like the one below:

```
$ locale -a
C
C.UTF-8
en_GB.utf8
POSIX
```

To generate new locales, run `sudo dpkg-reconfigure locales` and select any other desired locales. Here is a [useful list](http://www.localeplanet.com/icu/iso639.html) of ISO 639 language codes. **Important**: be sure to select UTF-8 as this is the preferred encoding. 

For example, on an RPi with many locales installed, `locale -a` would output something like this:

```
$ locale -a
C			# fall-back, ASCII encoding, same as POSIX
de_DE.utf8		# German language,     Germany,     UTF-8 encoding
fr_FR.utf8		# French language,     France,      UTF-8 encoding
it_IT.utf8		# Italian language,    Italy,       UTF-8 encoding
ja_JP.utf8		# Japanese language,   Japan,       UTF-8 encoding
en_GB.utf8		# English language,    GB,          UTF-8 encoding
en_US.utf8		# English language,    USA,         UTF-8 encoding
pt_BR.utf8		# Portuguese language, Brazil,      UTF-8 encoding
POSIX			# fall-back, ASCII encoding, same as C
```

Once you've configured a locale on your system, RaspAP will read the `HTTP_ACCEPT_LANGUAGE` string and use this to load your desired language in the UI. Alternatively, you can also select a different language from the  **Language** tab in the **System** menu.

![](https://i.imgur.com/mvB1lXf.png)

**Important**: If you configured a new locale after installing RaspAP, you must restart lighttpd for the changes to take effect:

```
sudo systemctl restart lighttpd.service
```

## Supported languages 

The following translations are currently maintained by the project: 

| Language | Locale | 
|---|---|
| Deutsch  | de_DE.UTF-8 |
| Dansk  | da_DK.UTF-8 |
| Français  | fr_FR.UTF-8 |
| Italiano | it_IT.UTF-8 |
| Português | pt_BR.UTF-8 |
| Svenska | sv_SE.UTF-8 |
| Nederlands | nl_NL.UTF-8 |
| 正體中文 (Chinese traditional) | zh_TW.UTF-8 |
| 简体中文 (Chinese simplified) | zh_CN.UTF-8 |
| Indonesian | id_ID.UTF-8 |
| 한국어 (Korean) | ko_KR.UTF-8 |
| 日本語 (Japanese) | ja_JP.UTF-8 |
| Tiếng Việt | vi_VN.UTF-8 |
| Čeština | cs_CZ.UTF-8 |
| Русский | ru_RU.UTF-8 |
| Polskie | pl_PL.UTF-8 |
| Español | es_MX.UTF-8 |
| Finnish | fi_FI.UTF-8 |
| Türkçe  | tr_TR.UTF-8 |
| ελληνικό | el_GR.UTF-8 |

We are certainly not limited to the above. If you are willing and able to translate RaspAP in your language, you will be credited as the original translator.

## Contributing to a translation
RaspAP now has a translation [project home at Crowdin](https://crowdin.com/project/raspap). This is the place to go for all volunteers who would like to contribute to our ongoing translation efforts. 

### How to become a translator
The process is very straightforward. Start by signing up for a free account at [Crowdin](https://crowdin.com/). Once you are logged in, head over to our [project home](https://crowdin.com/project/raspap). 

![Crowdin](https://i.imgur.com/pDUIXm6.jpg)

Here you will find our supported translations, recent activity, discussions and so on. You can get started by simply choosing the language you'd like to contribute to. For more info, see Crowdin's [detailed walkthrough](https://support.crowdin.com/crowdin-intro/#translation-process) of the translation process.

