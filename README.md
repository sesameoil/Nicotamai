# Nicotamai

ファイルを二子玉舞に変換します  
Encode file 二子玉舞

## ライセンス Licence

CC0 1.0 Universal.
See Also LICENCE, or [https://creativecommons.org/publicdomain/zero/1.0/legalcode](https://creativecommons.org/publicdomain/zero/1.0/legalcode).

## インストール Install

```
$ python3 -m pip install git+https://github.com/sesameoil/Nicotamai.git
```

or

```
$ git clone https://github.com/sesameoil/Nicotamai.git
$ python3 -m pip install ./Nicotamai
```

## アンインストール Uninstall

```
$ python3 -m pip uninstall nicotamai
```

## 使い方 Usage

### 変換 Encode

```
$ nicotamai [IN_FILE] [OUT_FILE]
```

例  Example

```
$ echo abc > hoge
$ nicotamai hoge fuga
$ cat fuga
子玉二子子玉二玉子玉二舞二二玉玉
```
`IN_FILE` が  `-` のとき、標準入力を読みます。  
`OUT_FILE` が  `-`のとき、 標準出力に書き込みます。  
When `IN_FILE`  is  `-` , read standard input.  
When `OUT_FILE` is  `-` , write standard output.  
  
例 Example

```
$ echo abc | nicotamai - -
子玉二子子玉二玉子玉二舞二二玉玉
```

`二子玉舞`が出現するたびに改行されます。  
Insert `\n` every after `二子玉舞`.

```
$ echo lm | nicotamai - -
子玉舞二子玉舞
子二二玉玉
```

### 復号 Decode

```
$ nicotamai -d [IN_FILE] [OUT_FILE]
```

例 Example

```
$ echo 子玉二子子玉二玉子玉二舞二二玉玉 > hoge
$ nicotamai -d hoge fuga
$ cat fuga
abc
```

`IN_FILE` が  `-` のとき、標準入力を読みます。  
`OUT_FILE` が  `-`のとき、 標準出力に書き込みます。  
When `IN_FILE` is `-`, read standard input.  
When `OUT_FILE` is `-`, write standard output.

例 Example

```
$ echo 子玉二子子玉二玉子玉二舞二二玉玉 | nicotamai -d - -
abc
```
