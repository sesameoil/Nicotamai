# Nicotamai

Encode binary 二子玉舞

## Licence

CC0 1.0 Universal.
See Also LICENCE, or [https://creativecommons.org/publicdomain/zero/1.0/legalcode](https://creativecommons.org/publicdomain/zero/1.0/legalcode).

## Install

```
$ python3 -m pip install git+https://github.com/sesameoil/Nicotamai.git
```

or

```
$ git clone https://github.com/sesameoil/Nicotamai.git
$ python3 -m pip install ./Nicotamai
```

## Uninstall

```
python3 -m pip uninstall nicotamai
```

## Usage

### Encode

```
$ nicotamai [IN_FILE] [OUT_FILE]
```

Example

```
$ echo abc > hoge
$ nicotamai hoge fuga
$ cat fuga
子玉二子子玉二玉子玉二舞二二玉玉
```

When [IN_FILE]  is  - , read standard input.  
When [OUT_FILE] is  - , write standard output.  
  
Example

```
$ echo abc | nicotamai - -
子玉二子子玉二玉子玉二舞二二玉玉
```

Insert New lines every after **二子玉舞**

```
$ echo lm | nicotamai - -
子玉舞二子玉舞
子二二玉玉
```

### Decode

```
$ echo 子玉二子子玉二玉子玉二舞二二玉玉 > hoge
$ nicotamai -d hoge fuga
$cat fuga
abc
```

When IN_FILE is **-**, read standard input.  
When OUT_FILE is **-**, write standard output. 
  
Example

```
echo 子玉二子子玉二玉子玉二舞二二玉玉 | nicotamai -d - -
abc
```
