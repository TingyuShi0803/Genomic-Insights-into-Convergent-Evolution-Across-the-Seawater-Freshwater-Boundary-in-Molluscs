import os

def generate_ctl_files(file_list):
    with open(file_list, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                # 从序列文件名中提取OG编号
                og_number = os.path.splitext(os.path.basename(line))[0]
               
                output_file = f"{og_number}"

               #下方所有控制条件需要自己更改。
                ctl_content = f"""seqfile = 你的目录/{og_number}.phy
treefile = 你的目录/{og_number}.treefile
outfile = 你的目录/{output_file}.ctl

noisy = 4 #####以下更换为你自己的测试信息
verbose = 1
runmode = 0

seqtype = 1
CodonFreq = 0
estFreq = 0

ndata = 1
clock = 0
aaDist = 0

model = 0

NSsites = 0 1 2 7 8

icode = 0
Mgene = 0

fix_kappa = 0
kappa = 2
fix_omega = 0
omega = 0.4

fix_alpha = 1
alpha = 0
Malpha = 0
ncatG = 5

getSE = 1
RateAncestor = 0

Small_Diff = 1e-5
cleandata = 0
fix_blength = 0
method = 0"""

                # 将ctl内容写入文件
                with open(f"{og_number}.ctl", "w") as ctl_file:
                    ctl_file.write(ctl_content)

file_list = "filename.fa"  # 替换为包含所有文件名的文件路径


generate_ctl_files(file_list)
