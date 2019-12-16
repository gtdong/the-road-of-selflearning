
from git import Repo

from git import Git
r=Repo("D:\\新电脑\\cw")
# git add
# r.index.add(["issue/utils/gitfile.py"])
#git commit -m
# r.index.commit("python 操作git")
#git reset HEAD  将缓存区的内容拉取到工作区
#git checkout filename 将指定文件回滚到最近一次commit的地方
#git reset --hard 将文件回滚到指定的位置
# r.index.reset(commit="e11f478c2e99e69969caf6e190751244d7b4608d",head=True)
# git branch
# r.branches
# 获取所有的分支
# print([str(b) for b in r.branches])
#git tag
#print(r.tags)
#当前分支
#print(r.active_branch)
#???
# r.index.checkout("dev1")
# git clone
#Repo.clone_from()
# git tag -a
# r.create_tag("v1.3")
# git branch dev4
# r.create_head("dev4")
# git log
print([i.message for i in r.iter_commits("master")])
#git push origin master
# r.remote().push("master")
#git pull origin master
# r.remote().pull("master")

# r=Git("C:\\Users\\Administrator\\Desktop\\derek")
# r.add(".")
# r.commit("-m 提交记录")

# r.checkout("dev4")