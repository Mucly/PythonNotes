# json库的使用
```python
    import json
    
    # json对象
    json_data = {
      "results": [
          {
              "location":
              {
                  "id": "WX4FBXXFKE4F",
                  "name": "北京",
                  "country": "CN",
                  "path": "北京,北京",
                  "timezone": "Asia/Shanghai",
                  "timezone_offset": "+08:00"
              }
          }]
    }

    # dump ： 将json_dict => str，并写入到file_obj
    # dumps： 不写入file_obj
    with open("j.json", 'w') as f:
      json.dump(json_data, f)

    # load ： 将str => json_dict，并写入到file_obj
    # loads： 不写入file_obj
    with open('j.json') as f:
      a = json.load(f)
      print(a)
```
