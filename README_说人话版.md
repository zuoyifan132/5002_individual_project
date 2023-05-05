# 测试指南-说人话版

Step1:将你的测试数据放入data/目录下，zip或者解压后的文件夹都可以。

Step2:将你的代码放入pytorch/tests/ 目录下，zip或者解压后的文件夹都可以

Step3:

```bash
cd pytorch
python evaluation.py
```

## 代码结构

```
   ./your-folder-name         (rename it acording to your setting)
   | --- __init__.py         
   | --- predict.py           (required) (rename it acording to your setting)
   | --- prepare.py           (required) (DO NOT rename it)
   | --- ... 
   | --- ./your-model-folder  (optional)
   | --- ... 
```

代码结构可以参考tests/目录下官方给的test-1.zip的结构，也可以参考我给的submit的结构，submit.zip来源于https://github.com/BUAABIGSCity/KDDCUP2022。



## ！！！如何当懒狗

如果想当懒狗，可以直接用我给出的submit测试全量数据集https://www.dropbox.com/s/l3rf8s6xbt5wn8o/final_phase_test.zip?dl=0。下载好之后解压直接放到data/文件夹下，并修改pytorch/evaluation.py中下面四行文件。注释掉下面两行，并打开上面两行

```python
    # TAR_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../data/final_phase_test/outfile'))
    # PRED_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../data/final_phase_test/infile'))
    
    TAR_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../data/sdwpf_baidukddcup2022_test_toy/test_y.zip'))
    PRED_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../data/sdwpf_baidukddcup2022_test_toy/test_x.zip'))
```



并且修改NUM_MAX_RUNS = 1为142。如果不修改的话只会eval第一个csv！！！！！全量数据集有142个csv！！！！！！





## 注意事项

请尽量不要直接用我给的submit来交差，否则容易被判定为学术造假，仅作为一个测试平台提供给大家。
