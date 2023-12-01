import pandas as pd
import json

def read_excel_keep_columns(file_path, columns,output_json_data):
    # 读取Excel文件
    df = pd.read_excel(file_path)
    
    # 保留指定的列
    df = df[columns]
    
    # 删除所有指定列都为空的行
    df = df.dropna(how='all', subset=['Market.01a_OE','Market.01b_OE','Market.01c_OE'])
    
    # 构建微调数据文件
    data_list = df.values.tolist()
    json_data_list = []
    for bg,q1,q2,q3,score,r1,r2,r3 in data_list:
        bg = bg.replace("\n","")
        if r1!='idk' and r1 !='na' and r1 !='NA':
            # 'Hello {0}! My name is {1}.'.format('World', 'Python猫')
            r1 = str(r1).replace("\n","")
            json_data = {
                "instruction":"Please combine the question and score the student's response. The scoring range is 0 to 4 points.",
                "input":"background:{0};question:{1};answer:{2}".format(bg,q1,r1),
                "output":score
            }
            json_data_list.append(json_data)
        if r2!='idk' and r2 !='na' and r2 !='NA':
            r2 = str(r2).replace("\n","")
            # 'Hello {0}! My name is {1}.'.format('World', 'Python猫')
            json_data = {
                "instruction":"Please combine the question and score the student's response. The scoring range is 0 to 4 points.",
                "input":"background:{0};question:{1};answer:{2}".format(bg,q2,r2),
                "output":score
            }
            json_data_list.append(json_data)
        if r3!='idk' and r3 !='na' and r3 !='NA':
            r3 = str(r3).replace("\n","")
            # 'Hello {0}! My name is {1}.'.format('World', 'Python猫')
            json_data = {
                "instruction":"Please combine the question and score the student's response. The scoring range is 0 to 4 points.",
                "input":"background:{0};question:{1};answer:{2}".format(bg,q3,r3),
                "output":score
            }
            json_data_list.append(json_data)
        
        # 将数据写入 JSON 文件
    
    with open(output_json_data, 'w') as json_file:
        json.dump(json_data_list, json_file)
    print('json 微调数据写入 成功 ')

# Excel文件路径
file_path = '/root/autodl-tmp/LLM-ALL-SFT/llm_sft/dataset/origin_data.xlsx'
output_json_data = '/root/autodl-tmp/LLM-ALL-SFT/llm_sft/dataset/student_score.json'
# 你想保留的四列列名
# background	question_01	question_02	question_03	Score	Market.01a_OE	Market.01b_OE	Market.01c_OE
columns_to_keep = ['background', 'question_01', 'question_02', 'question_03','Score','Market.01a_OE','Market.01b_OE','Market.01c_OE']

# 调用函数
read_excel_keep_columns(file_path, columns_to_keep,output_json_data)

