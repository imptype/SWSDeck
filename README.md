# SWSDeck

A quick helper API to generate a [Stick War Saga][1] deck image from a URL.

Icons were obtained by slicing them out of 1920x1080 screenshots ([slice.py][2]).

To use, append the url with a query string like `?123123` to get 8 cards of IDs 1, 2, 3, 1, 2, 3, -, -.

To see the full list of IDs, omit the query string. Invalid IDs default to a blank card.

All game content is © [Max Games][2]. This project is unofficial and for non-commercial, fan-made purposes only.

[1]: https://play.google.com/store/apps/details?id=com.maxgames.stickwar3
[2]: ./slice.py  
[3]: https://www.maxgames.com/