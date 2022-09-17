# UC
一个简化uniCloud cli开发的工具
## 应用场景
在使用 uniCloud 开发时，需要调用Hbuilder进行云函数的上传，如果不想使用Hbuilder上传云函数，可以采用cli的方式，但cli方式命令行过长，且不易使用，本工具便简化其使用。

## 如何使用
下载Releases内最符合您操作系统的版本，将uc.exe 文件放置在您的运行目录下，首次运行会在当前目录下生成一个ucConfig.json文件，请使用记事本或者编辑器打开该文件，并将hbuilder运行目录填写在hbuilder对应的位置，object与provider不用填写，如：  
`
{
    "hbuilder":"D:\HbuilderX",
    "object":"",
    "provider":""
}
`  
填写之后，即可使用如下方法进行操作  
### 1. **列举资源信息**  
`uc.exe -l [resource]` 如 `uc.exe -l cf` 表示：列举当前项目中所有云端函数  
### 2. **资源上传[默认覆盖非跳过]**  
`uc.exe -u [resource] [name]` 如 `uc.exe -u cf test` 表示：上传名称为test的云函数，如果云端存在同名函数则覆盖  
### 3. **资源下载[默认覆盖非跳过]**  
`uc.exe -d [resource] [name]` 如 `uc.exe -d cf test` 表示：下载名称为test的云函数，如果本地存在同名函数则覆盖  
### 4. resource的取值如下  
|resource  | 含义 |  
| ----------- | ----------- |  
| cf 或 cloudfunction | 云函数 |  
| cm 或 common | 云函数的公共模块 |  
| db | 数据集合Schema |  
| vf | 数据库校验函数  |  
| ac 或 action | 数据库触发条件 |  
| sp 或 space | 云空间 |  

## 关于作者
[歪克士的博客](https://wicos.me)


