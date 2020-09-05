# Wooosh

Deobfuscate all the code and after finding this line

```text
socket['emit']('click', coords[0x0], coords[0x1]);
```

This sends a post that'll send mouse coords. after i messed around a bit i realised that the shapes coords are different from the one they send to you so i guess something happens with them \(not sure what tho\). i then analysed the thingies going on in network which was always in the pattern start \[get shapes, send coords, get score\] and found the code to find mouse coords \(see deobfuscated js\) was consistent with where the shapes are displayed. after that i looked at the code that draws out the shapes with the coord and figured out how it knows whether to draw a circle or square. which was:

```javascript
function drawShapes() {
    ctx["clearRect"](0x0, 0x0, 0x1f4, 0x12c);
    shapes['map'](
        (_0x401a13,_0x53031c)=>_0x53031c ? ctx["fillRect"](_0x401a13['x'] - 0x5, _0x401a13['y'] - 0x5, 0xa, 0xa) 
        : ctx['beginPath']() + ctx["arc"](_0x401a13['x'], _0x401a13['y'], 0x5, 0x0, Math['PI'] * 0x2) + ctx["closePath"]() + ctx["fill"]()
        );
```

If you know a little js, it chooses the first element of the shapes list to be a circle and the rest are squares. after that i checked whether the shapes list matches the shapes list going in through the network and found they were different. The shapes list was correct and matched the coords of the circle and after analysing a thingy that sends my mouse coords, they were roughly the same which meant i could create the payload

```text
socket['emit']('click', shapes[0].x, shapes[0].y);
```

Spam it through console when i press start which gave me points :\) and then i got the flag \(turns out i didnt need the backend source code lol\)

## actf{w0000sh\_1s\_th3\_s0und\_0f\_th3\_r3qu3st\_fly1ng\_p4st\_th3\_fr0nt3nd}

```javascript
var _0x1ce0 = ['bWFw', 'SlBOcFY=', 'a1dQd2M=', 'Z2V0Q29udGV4dA==', 'SkxnSXA=', 'Y2xvc2VQYXRo', 'Y0dhbWU=', 'Y291bnRlcg==', 'Z2V0Qm91bmRpbmdDbGllbnRSZWN0', 'c3RhdGVPYmplY3Q=', 'QmZDSk0=', 'WVlOdEU=', 'ZmlsbA==', 'TWZhRHU=', 'c3BsaXQ=', 'TnNndkw=', 'd2Fybg==', 'ck9ZWHg=', 'UnNGSFI=', 'b3dsQnU=', 'RkRCaGY=', 'eERtaWc=', 'cVZyYms=', 'dEtxZXQ=', 'YllhZFQ=', 'UVJWcVA=', 'eFJkWUM=', 'QUdRZnU=', 'UUR3cHc=', 'Tk9Cam4=', 'bUJ2QU8=', 'Z2V0RWxlbWVudEJ5SWQ=', 'Y2xpZW50WA==', 'bGVuZ3Ro', 'ZXhjZXB0aW9u', 'TmhncEI=', 'Q1VnV20=', 'QlFQYVI=', 'YWRkRXZlbnRMaXN0ZW5lcg==', 'Y29uc3RydWN0b3I=', 'YmVnaW5QYXRo', 'YUpBbHU=', 'aW5pdA==', 'Y1h0TGY=', 'cHh0Q2Y=', 'XCtcKyAqKD86W2EtekEtWl8kXVswLTlhLXpBLVpfJF0qKQ==', 'ZXd3YUE=', 'ZGlzY29ubmVjdA==', 'SUp4T0w=', 'QmlRb1Y=', 'cmV0dXJuIC8iICsgdGhpcyArICIv', 'S09Bd1E=', 'V0ZtVHQ=', 'bmF0Qm8=', 'dlFSdEU=', 'I2ZmMDAwMA==', 'Y29uc29sZQ==', 'VEJXUWk=', 'SGl0bEI=', 'ZW95Y1g=', 'YWF0U24=', 'UU5Pc3I=', 'a2ZPREk=', 'UkhqWGU=', 'ZGVidWc=', 'QlZnUEI=', 'bENjSEo=', 'cFhQRkw=', 'bnBLSEU=', 'ZXJyb3I=', 'e30uY29uc3RydWN0b3IoInJldHVybiB0aGlzIikoICk=', 'Y2FsbA==', 'T2ROVEE=', 'dG9w', 'b2Jlemg=', 'U1dvS0Y=', 'c2hhcGVz', 'eXRJbkE=', 'Y3NheFE=', 'ZnVuY3Rpb24gKlwoICpcKQ==', 'bG9n', 'V3ZJQ3o=', 'anhGSm8=', 'YXhFRW8=', 'cGVKYlY=', 'WFZRU1A=', 'REdEcUU=', 'dGFibGU=', 'bnlmTlc=', 'dkJmanI=', 'd3lJVVA=', 'Y2xpY2s=', 'UXJYaGo=', 'ZFVoano=', 'cmV0dXJuIChmdW5jdGlvbigpIA==', 'XihbXiBdKyggK1teIF0rKSspK1teIF19', 'QURlbWk=', 'VEpEWmk=', 'VWRBTFo=', 'WWpXaXI=', 'elFyalM=', 'Mnw1fDl8OHwxfDZ8N3wwfDR8Mw==', 'aW5wdXQ=', 'd2hpbGUgKHRydWUpIHt9', 'QWZBT1M=', 'WmZNeFc=', 'dHJhY2U=', 'RVBublU=', 'Z2dlcg==', 'UEtrQmg=', 'Y2xlYXJSZWN0', 'YXJj', 'dGVzdA==', 'c2NvcmU=', 'bktJanY=', 'Y2hhaW4=', 'Q2Z1V0o=', 'U2NvcmU6IA==', 'SlV0dVY=', 'ZmlsbFN0eWxl', 'YlN0YXJ0', 'aW5GREs=', 'SERnSEY=', 'VlN0TG8=', 'ZmlsbFJlY3Q=', 'WHhaaXc=', 'c3RhcnQ=', 'YXBwbHk=', 'NHwxfDV8N3w2fDN8Mnww', 'ZGVidQ==', 'ZW1pdA==', 'RUpoc08=', 'enFVUWo=', 'ZldOVGs=', 'V0ZibmY=', 'aW5mbw=='];
(function(_0x20cc64, _0x1ce09b) {//cookie stuff 
    var _0x34d7a6 = function(_0x45c586) {
        while (--_0x45c586) {
            _0x20cc64['push'](_0x20cc64['shift']());
        }
    };
    var _0x59c786 = function() {
        var _0x2ee600 = {
            'data': {
                'key': 'cookie',
                'value': 'timeout'
            },
            'setCookie': function(_0x1baf97, _0x584a1c, _0x27dfce, _0x2f47ff) {
                _0x2f47ff = _0x2f47ff || {};
                var _0x3cdb63 = _0x584a1c + '=' + _0x27dfce;
                var _0x3ab829 = 0x0;
                for (var _0x30b65a = 0x0, _0x2024f0 = _0x1baf97['length']; _0x30b65a < _0x2024f0; _0x30b65a++) {
                    var _0x1e37b5 = _0x1baf97[_0x30b65a];
                    _0x3cdb63 += ';\x20' + _0x1e37b5;
                    var _0x1dca17 = _0x1baf97[_0x1e37b5];
                    _0x1baf97['push'](_0x1dca17);
                    _0x2024f0 = _0x1baf97['length'];
                    if (_0x1dca17 !== !![]) {
                        _0x3cdb63 += '=' + _0x1dca17;
                    }
                }
                _0x2f47ff['cookie'] = _0x3cdb63;
            },
            'removeCookie': function() {
                return 'dev';
            },
            'getCookie': function(_0x3962bf, _0x49db25) {
                _0x3962bf = _0x3962bf || function(_0x506876) {
                    return _0x506876;
                }
                ;
                var _0x3b872e = _0x3962bf(new RegExp('(?:^|;\x20)' + _0x49db25['replace'](/([.$?*|{}()[]\/+^])/g, '$1') + '=([^;]*)'));
                var _0x21d4b7 = function(_0xaa6690, _0x5f084e) {
                    _0xaa6690(++_0x5f084e);
                };
                _0x21d4b7(_0x34d7a6, _0x1ce09b);
                return _0x3b872e ? decodeURIComponent(_0x3b872e[0x1]) : undefined;
            }
        };
        var _0x37cabe = function() {
            var _0x27a400 = new RegExp('\x5cw+\x20*\x5c(\x5c)\x20*{\x5cw+\x20*[\x27|\x22].+[\x27|\x22];?\x20*}');
            return _0x27a400['test'](_0x2ee600['removeCookie']['toString']());
        };
        _0x2ee600['updateCookie'] = _0x37cabe;
        var _0xc4302b = '';
        var _0x2d1069 = _0x2ee600['updateCookie']();
        if (!_0x2d1069) {
            _0x2ee600['setCookie'](['*'], 'counter', 0x1);
        } else if (_0x2d1069) {
            _0xc4302b = _0x2ee600['getCookie'](null, 'counter');
        } else {
            _0x2ee600['removeCookie']();
        }
    };
    _0x59c786();
}(_0x1ce0, 0xed));
var _0x34d7 = function(_0x20cc64, _0x1ce09b) {
    _0x20cc64 = _0x20cc64 - 0x0;
    var _0x34d7a6 = _0x1ce0[_0x20cc64];
    if (_0x34d7['ptmszC'] === undefined) {//ignore this below, values are decoded b64 from _0x1ce0. if statement checks if the values have been decoded already
        (function() {
            var _0x45c586 = function() {
                var _0xc4302b;
                try {
                    _0xc4302b = Function('return\x20(function()\x20' + '{}.constructor(\x22return\x20this\x22)(\x20)' + ');')();
                } catch (_0x2d1069) {
                    _0xc4302b = window;
                }
                return _0xc4302b;
            };
            var _0x2ee600 = _0x45c586();
            var _0x37cabe = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=';
            _0x2ee600['atob'] || (_0x2ee600['atob'] = function(_0x1baf97) {
                var _0x584a1c = String(_0x1baf97)['replace'](/=+$/, '');
                var _0x27dfce = '';
                for (var _0x2f47ff = 0x0, _0x3cdb63, _0x3ab829, _0x30b65a = 0x0; _0x3ab829 = _0x584a1c['charAt'](_0x30b65a++); ~_0x3ab829 && (_0x3cdb63 = _0x2f47ff % 0x4 ? _0x3cdb63 * 0x40 + _0x3ab829 : _0x3ab829,
                _0x2f47ff++ % 0x4) ? _0x27dfce += String['fromCharCode'](0xff & _0x3cdb63 >> (-0x2 * _0x2f47ff & 0x6)) : 0x0) {
                    _0x3ab829 = _0x37cabe['indexOf'](_0x3ab829);
                }
                return _0x27dfce;
            }
            );
        }());
        _0x34d7['pwjwqN'] = function(_0x2024f0) {
            var _0x1e37b5 = atob(_0x2024f0);
            var _0x1dca17 = [];
            for (var _0x3962bf = 0x0, _0x49db25 = _0x1e37b5['length']; _0x3962bf < _0x49db25; _0x3962bf++) {
                _0x1dca17 += '%' + ('00' + _0x1e37b5['charCodeAt'](_0x3962bf)['toString'](0x10))['slice'](-0x2);
            }
            return decodeURIComponent(_0x1dca17);
        }
        ;
        _0x34d7['psiqcL'] = {};
        true = !![];
    }
    var _0x59c786 = _0x34d7['psiqcL'][_0x20cc64];
    if (_0x59c786 === undefined) {
        var _0x3b872e = function(_0x21d4b7) {
            this['FnKpUT'] = _0x21d4b7;
            this['dnpwlO'] = [0x1, 0x0, 0x0];
            this['xxqOHK'] = function() {
                return 'newState';
            }
            ;
            this['UFWVYh'] = '\x5cw+\x20*\x5c(\x5c)\x20*{\x5cw+\x20*';
            this['okSRxK'] = '[\x27|\x22].+[\x27|\x22];?\x20*}';
        };
        _0x3b872e['prototype']['zRoycw'] = function() {
            var _0x506876 = new RegExp(this['UFWVYh'] + this['okSRxK']);
            var _0xaa6690 = _0x506876['test'](this['xxqOHK']['toString']()) ? --this['dnpwlO'][0x1] : --this['dnpwlO'][0x0];
            return this['wWoyOu'](_0xaa6690);
        }
        ;
        _0x3b872e['prototype']['wWoyOu'] = function(_0x5f084e) {
            if (!Boolean(~_0x5f084e)) {
                return _0x5f084e;
            }
            return this['Mmnboh'](this['FnKpUT']);
        }
        ;
        _0x3b872e['prototype']['Mmnboh'] = function(_0x27a400) {
            for (var _0x4f73b9 = 0x0, _0x317d20 = this['dnpwlO']['length']; _0x4f73b9 < _0x317d20; _0x4f73b9++) {
                this['dnpwlO']['push'](Math['round'](Math['random']()));
                _0x317d20 = this['dnpwlO']['length'];
            }
            return _0x27a400(this['dnpwlO'][0x0]);
        }
        ;
        new _0x3b872e(_0x34d7)['zRoycw']();
        _0x34d7a6 = _0x34d7['pwjwqN'](_0x34d7a6);
        _0x34d7['psiqcL'][_0x20cc64] = _0x34d7a6;
    } else {
        _0x34d7a6 = _0x59c786;
    }
    return _0x34d7a6;
};
var _0x2f47ff = function() {
    var _0x34a890 = {
        'xDmig': function(_0x1acd1d, _0x50045b) {
            return _0x1acd1d === _0x50045b;
        },
        'FDBhf': "npKHE",
        'AWOLM': "while (true) {}",
        'RZUwZ': "counter",
        'eoycX': "QNOsr",
        'cXtLf': 'BuBbm'
    };
    var _0x418c8e = !![];
    return function(_0x28cb74, _0x39da2d) {
        var _0x22e999 = {
            'EPnnU': "while (true) {}",
            'ZfMxW': "counter"
        };
        if (false) {
            if (_0x39da2d) {
                var _0xdc044d = _0x39da2d["apply"](_0x28cb74, arguments);
                _0x39da2d = null;
                return _0xdc044d;
            }
        } else {
            var _0x32fd69 = _0x418c8e ? function() {
                if (true) {//this bit is the only part that runs
                    if (_0x39da2d) { //true
                        var _0x4f6b34 = _0x39da2d["apply"](_0x28cb74, arguments);
                        _0x39da2d = null;
                        return _0x4f6b34;
                    }
                } else { //never executes
                    return function(_0x18294d) {}
                    ["constructor"]("while (true) {}")["apply"]("counter");
                }
            }
            : function() {} //this never runs
            ;
            _0x418c8e = ![];
            return _0x32fd69;
        }
    }
    ;
}();
var _0x27dfce = _0x2f47ff(this, function() {
    var _0x4d850d = {
        'DGDqE': function(_0x3dac4c, _0xd908d4) {
            return _0x3dac4c === _0xd908d4;
        },
        'QRVqP': "JLgIp",
        'MfaDu': "return /" + this + "/",
        'axEEo': "^([^ ]+( +[^ ]+)+)+[^ ]}"
    };
    var _0x4104ec = function() {
        if (true) {
            var _0x1baf6d = _0x4104ec['constructor']("return /" + this + "/")()['compile']("^([^ ]+( +[^ ]+)+)+[^ ]}");
            return !_0x1baf6d["test"](_0x27dfce);
        } else { //never executes
            that['console'] = function(_0x54cc65) {
                var _0x521582 = {};
                _0x521582["log"] = _0x54cc65;
                _0x521582["warn"] = _0x54cc65;
                _0x521582["debug"] = _0x54cc65;
                _0x521582["info"] = _0x54cc65;
                _0x521582["error"] = _0x54cc65;
                _0x521582["exception"] = _0x54cc65;
                _0x521582["table"] = _0x54cc65;
                _0x521582['trace'] = _0x54cc65;
                return _0x521582;
            }(func);
        }
    };
    return _0x4104ec();
});
_0x27dfce();
var _0x1baf97 = function() {
    var _0x4a04d8 = {
        'QDwpw': function(_0x580bda, _0xde7f8) {
            return _0x580bda === _0xde7f8;
        },
        'OdNTA': "kWPwc",
        'wuTZe': "XxZiw",
        'tKqet': 'ebwEc'
    };
    var _0x2e098e = !![];
    return function(_0x144f1d, _0x210b4a) {
        var _0x431a70 = {
            'mBvAO': function(_0x4bfe9c, _0x32222e) {
                return _0x4bfe9c === _0x32222e;
            },
            'UdALZ': "kWPwc",
            'nyfNW': "XxZiw",
            'acHtD': 'ebwEc'
        };
        var _0x388e28 = _0x2e098e ? function() {
            if (false) {
                msg = m;
                update();
            } else {
                if (_0x210b4a) {
                    if (false) {
                        var _0x37f6ab = _0x210b4a['apply'](_0x144f1d, arguments);
                        _0x210b4a = null;
                        return _0x37f6ab;
                    } else { //does same thing
                        var _0x4b2e75 = _0x210b4a["apply"](_0x144f1d, arguments);
                        _0x210b4a = null;
                        return _0x4b2e75;
                    }
                }
            }
        }
        : function() {}
        ;
        _0x2e098e = ![];
        return _0x388e28;
    }
    ;
}();
(function() {
    var _0x32f2b7 = {
        'natBo': "function *\( *\)",
        'SWoKF': '\x5c+\x5c+\x20*(?:[a-zA-Z_$][0-9a-zA-Z_$]*)',
        'TJDZi': function(_0x383e42, _0x247ec9) {
            return _0x383e42 + _0x247ec9;
        },
        'ytInA': function(_0x11e1a6, _0x3012cc) {
            return _0x11e1a6 + _0x3012cc;
        },
        'ADemi': "input",
        'rOYXx': "fWNTk",
        'GhaAN': function(_0x4d7529, _0x4cb76f) {
            return _0x4d7529(_0x4cb76f);
        },
        'SGiMY': "init",
        'aatSn': function(_0x4b2ee6, _0x4523dd) {
            return _0x4b2ee6 + _0x4523dd;
        },
        'jxFJo': "chain",
        'RsFHR': function(_0x5a9552, _0x34a4f2) {
            return _0x5a9552 + _0x34a4f2;
        },
        'zQrjS': function(_0x533fe7) {
            return _0x533fe7();
        }
    };
    _0x1baf97(this, function() {
        var _0x459fa1 = { //creates copy
            'xgOqS': "function *\( *\)",
            'YjWir': '\x5c+\x5c+\x20*(?:[a-zA-Z_$][0-9a-zA-Z_$]*)',
            'SvEXK': function(_0x5b2268, _0x20ad34) {
                return _0x5b2268(_0x20ad34);
            },
            'qVrbk': function(_0x4d1237, _0x4cd30e) {
                return _0x4d1237 + _0x4cd30e;
            },
            'IJxOL': "chain",
            'HitlB': function(_0x16d47a, _0x19706a) {
                return _0x16d47a + _0x19706a;
            },
            'WFmTt': "input",
            'zqUQj': function(_0x45146b, _0x15a3ad) {
                return _0x45146b(_0x15a3ad);
            },
            'JUtuV': function(_0x90fc88, _0x1f2352, _0x330dd0) {
                return _0x90fc88(_0x1f2352, _0x330dd0);
            }
        };
        if (true) { //actual code starts
            var _0x3db3a5 = new RegExp("function *\( *\)");
            var _0x4a74b1 = new RegExp('\+\+ *(?:[a-zA-Z_$][0-9a-zA-Z_$]*)','i');
            var _0x516a0a = _0x2d1069("init"); //cookie stuff
            if (!_0x3db3a5['test'](_0x516a0a + "chain") || !_0x4a74b1["test"](_0x516a0a + "input")) {
                _0x516a0a('0');
            } else {
                _0x2d1069;
            }
        } else { //ignore this
            _0x459fa1["JUtuV"](_0x1baf97, this, function() {
                var _0x14a11a = new RegExp(_0x459fa1['xgOqS']);
                var _0x5167c5 = new RegExp(_0x459fa1["YjWir"],'i');
                var _0x35294f = _0x459fa1['SvEXK'](_0x2d1069, "init");
                if (!_0x14a11a["test"](_0x459fa1["qVrbk"](_0x35294f, _0x459fa1["IJxOL"])) || !_0x5167c5['test'](_0x459fa1["HitlB"](_0x35294f, _0x459fa1["WFmTt"]))) {
                    _0x459fa1["zqUQj"](_0x35294f, '0');
                } else {
                    _0x2d1069();
                }
            })();
        }
    })();
}());
var _0x2ee600 = function() {
    var _0x495ac2 = {
        'atoNo': 'KOAwQ',
        'csaxQ': 'lCcHJ'
    };
    var _0x349c1f = !![];
    return function(_0x433e6d, _0x5e0022) {
        var _0x48c3bc = _0x349c1f ? function() {
            if (false) {//ignore
                if (_0x5e0022) {
                    var _0x161cc2 = _0x5e0022['apply'](_0x433e6d, arguments);
                    _0x5e0022 = null;
                    return _0x161cc2;
                }
            } else {//basically do same things
                if (_0x5e0022) {
                    var _0x60f4d3 = _0x5e0022["apply"](_0x433e6d, arguments);
                    _0x5e0022 = null;
                    return _0x60f4d3;
                }
            }
        }
        : function() {}
        ;
        _0x349c1f = ![];
        return _0x48c3bc;
    }
    ;
}();
var _0x45c586 = _0x2ee600(this, function() {
    var _0x173ec1 = {
        'YYNtE': function(_0x31edf7, _0x1a2a90) {
            return _0x31edf7 + _0x1a2a90;
        },
        'TBWQi': function(_0x50c5e2, _0x145a68) {
            return _0x50c5e2 + _0x145a68;
        },
        'AGQfu': '2|5|9|8|1|6|7|0|4|3',
        'NOBjn': "return /" + this + "/",
        'WFbnf': "^([^ ]+( +[^ ]+)+)+[^ ]}",
        'xRdYC': function(_0x28078a) {
            return _0x28078a();
        },
        'bYadT': function(_0x1edb6d, _0x41b276) {
            return _0x1edb6d === _0x41b276;
        },
        'inFDK': 'wPbVg',
        'peJbV': '4|1|5|7|6|3|2|0'
    };
    var _0x5a2bbc = function() {};
    var _0x16f724 = function() {
        var _0x47e403;
        try {
            _0x47e403 = Function('return (function() {}.constructor("return this")( ));')();
        } catch (_0x3b48f1) {
            _0x47e403 = window;
        }
        return _0x47e403;
    };
    var _0x2386f1 = _0x16f724();
    if (!_0x2386f1['console']) {
        _0x2386f1['console'] = function(_0x368eaa) {
            var _0x95093c = ["2", "5", "9", "8", "1", "6", "7", "0", "4", "3"];
            var _0x495f14 = 0x0;
            while (true) {
                switch (_0x95093c[_0x495f14++]) { //iterate throught this
                case '0':
                    _0xd80574["table"] = _0x368eaa;
                    continue;
                case '1':
                    _0xd80574["info"] = _0x368eaa;
                    continue;
                case '2':
                    var _0xd80574 = {};
                    continue;
                case '3':
                    return _0xd80574;
                case '4':
                    _0xd80574['trace'] = _0x368eaa;
                    continue;
                case '5':
                    _0xd80574["log"] = _0x368eaa;
                    continue;
                case '6':
                    _0xd80574["error"] = _0x368eaa;
                    continue;
                case '7':
                    _0xd80574["exception"] = _0x368eaa;
                    continue;
                case '8':
                    _0xd80574['debug'] = _0x368eaa;
                    continue;
                case '9':
                    _0xd80574["warn"] = _0x368eaa;
                    continue;
                }
                break;
            }
        }(_0x5a2bbc);
    } else {
        if (true) {
            var _0xd32090 = ["4", "1", "5", "7", "6", "3", "2", "0"];
            var _0x64c580 = 0x0;
            while (true) {
                switch (_0xd32090[_0x64c580++]) {//iterate through this using list
                case '0':
                    _0x2386f1['console']['trace'] = _0x5a2bbc;
                    continue;
                case '1':
                    _0x2386f1['console']["warn"] = _0x5a2bbc;
                    continue;
                case '2':
                    _0x2386f1['console']["table"] = _0x5a2bbc;
                    continue;
                case '3':
                    _0x2386f1['console']["exception"] = _0x5a2bbc;
                    continue;
                case '4':
                    _0x2386f1['console']["log"] = _0x5a2bbc;
                    continue;
                case '5':
                    _0x2386f1['console']["debug"] = _0x5a2bbc;
                    continue;
                case '6':
                    _0x2386f1['console']["error"] = _0x5a2bbc;
                    continue;
                case '7':
                    _0x2386f1['console']["info"] = _0x5a2bbc;
                    continue;
                }
                break;
            }
        } else {
            var _0x3e1b1b = test['constructor']("return /" + this + "/")()['compile']("^([^ ]+( +[^ ]+)+)+[^ ]}");
            return !_0x3e1b1b["test"](_0x27dfce);
        }
    }
});
_0x45c586();
var socket = io();
var bStart = document['getElementById']('bStart');
var cGame = document['getElementById']('cGame');
var pScore = document['getElementById']('pScore');
var score = 0x0;
var msg = '';
var shapes = [];
var ctx = cGame['getContext']('2d');
function update() {
    pScore['innerHTML'] = 'Score: ' + score + (msg ? ',\x20' : '') + msg;
}
function drawShapes() {
    ctx["clearRect"](0x0, 0x0, 0x1f4, 0x12c);
    shapes['map'](
        (_0x401a13,_0x53031c)=>_0x53031c ? ctx["fillRect"](_0x401a13['x'] - 0x5, _0x401a13['y'] - 0x5, 0xa, 0xa) 
        : ctx['beginPath']() + ctx["arc"](_0x401a13['x'], _0x401a13['y'], 0x5, 0x0, Math['PI'] * 0x2) + ctx["closePath"]() + ctx["fill"]()
        );
}
function getCursorPosition(_0x2b237a, _0x380ec8) {
    var _0x127ab4 = {
        'NhgpB': function(_0x3d88ae, _0x1d8777) {
            return _0x3d88ae - _0x1d8777;
        }
    };
    const _0x17e5d8 = _0x2b237a['getBoundingClientRect']();
    const _0x4a40e = _0x380ec8['clientX'] - _0x17e5d8['left'];//90.5
    const _0x1efa5e = _0x380ec8['clientY'] -  _0x17e5d8['top'];//246.96875
    return [_0x4a40e, _0x1efa5e];
}
bStart['addEventListener']('click', function() {
    var _0x1cd630 = {
        'GYjuS': "start"
    };
    socket['emit']("start");
});
socket['on']('disconnect', function() {
    var _0xf6eed5 = {
        'nKIjv': 'You\x20have\x20been\x20disconnected.',
        'dUhjz': function(_0x3ebbbf) {
            return _0x3ebbbf();
        }
    };
    msg = 'You\x20have\x20been\x20disconnected.';
    update();
});
socket['on']('score', function(_0x3576f2) {
    score = _0x3576f2;
    update();
});
socket['on']('disp', function(_0x522d36) {
    var _0x1fe455 = {
        'JPNpV': function(_0x31be72) {
            return _0x31be72();
        }
    };
    msg = _0x522d36;
    update();
});
socket['on']('shapes', function(_0x327b9d) {
    var _0x312e90 = {
        'NsgvL': function(_0x2c843a) {
            return _0x2c843a();
        }
    };
    shapes = _0x327b9d;
    drawShapes();
});
ctx['fillStyle'] = '#ff0000';
cGame['addEventListener']('click', function(mousedata) {
    var _0x3c1dc7 = {
        'CfuWJ': function(_0x5ea446, _0x41976a, _0x3e4576) {
            return _0x5ea446(_0x41976a, _0x3e4576);
        }
    };
    var _0x2f570f = getCursorPosition( cGame, mousedata);
    socket['emit']('click', _0x2f570f[0x0], _0x2f570f[0x1]);
});
function _0x2d1069(_0x36830f) {
    var _0x30ad20 = {
        'VStLo': 'HDgHF',
        'owlBu': function(_0x368ec1, _0xc0219e) {
            return _0x368ec1 === _0xc0219e;
        },
        'BiQoV': 'kfODI',
        'BVgPB': 'string',
        'EPpzm': 'AfAOS',
        'pXPFL': 'QrXhj',
        'aJAlu': "counter",
        'wyIUP': function(_0x117ee9, _0xdaeb77) {
            return _0x117ee9 + _0xdaeb77;
        },
        'XVQSP': function(_0x3c2d14, _0x47006) {
            return _0x3c2d14 / _0x47006;
        },
        'nVazA': 'length',
        'obezh': function(_0x19cb7e, _0x71f6ca) {
            return _0x19cb7e % _0x71f6ca;
        },
        'EJhsO': 'gger',
        'RHjXe': 'action',
        'PKkBh': function(_0x33e933, _0x115743) {
            return _0x33e933 !== _0x115743;
        },
        'vBfjr': 'ewwaA',
        'WvICz': 'xcJlq',
        'pxtCf': 'debu',
        'OZmQc': function(_0xdb7a71, _0x5eafb1) {
            return _0xdb7a71(_0x5eafb1);
        },
        'BfCJM': function(_0x2f3450) {
            return _0x2f3450();
        },
        'BQPaR': 'vQRtE'
    };
    function _0x17b7f6(_0x23c200) {
        if (typeof _0x23c200 === 'string') {//checks if string but has to be a number  so wont run
            if (false) {
                return !![]; //true
            } else { //actual
                return function(_0x12ba0e) {}
                ["constructor"]("while (true) {}")["apply"]("counter");
            }
        } else {
            if ((_0x23c200 % 0x14) === 0x0) { //checks if divisible by 20
                (function() {
                    if (false) {
                        return ![];
                    } else {
                        return !![]; //true
                    }
                }
                ["constructor"]('debugger')['call']("action"));
            } else {
                if (true) {
                    (function() {
                        if (false) {
                            ctx["clearRect"](0x0, 0x0, 0x1f4, 0x12c);
                            shapes["map"]((_0x16827f,_0x45d640)=>_0x45d640 ? ctx["fillRect"](_0x16827f['x'] - 0x5, _0x16827f['y'] - 0x5, 0xa, 0xa) : ctx["map"]() + ctx["arc"](_0x16827f['x'], _0x16827f['y'], 0x5, 0x0, Math['PI'] * 0x2) + ctx["closePath"]() + ctx["fill"]());
                        } else {
                            return ![]; //false
                        }
                    }
                    ["constructor"]("debugger")["apply"]('stateObject'));
                } else {
                    return _0x17b7f6;
                }
            }
        }
        _0x17b7f6(++_0x23c200);
    }
    try {
        if (_0x36830f) {
            if (true) {
                return _0x17b7f6;
            } else {
                score = sc;
                update();
            }
        } else {
            _0x17b7f6(0x0);
        }
    } catch (_0x1185a1) {}
}
```

