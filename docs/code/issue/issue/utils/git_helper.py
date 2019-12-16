from git import Repo
from git import Git
import os
class GitHelper():

    def __init__(self,path):
        self.path=path

    def is_dir(self,url):
        print(self.path)
        path=os.path.join(self.path,".git")
        if not os.path.exists(path):
              Repo.clone_from(url,self.path)

    def get_branch(self):
        return [str(br).split("/")[1] for br in Repo(self.path).remote().refs if str(br)!="origin/HEAD"]

    def get_commit(self,bra):
        #下载
        # Repo(self.path).remote().pull(bra)

        #获取当前所在的分支
        try:
            active=Repo(self.path).active_branch
        except Exception as e:
            active="master"
        print(active)
        #强制将本地的内容与本地仓库保持一致
        Repo(self.path).index.reset(commit="origin/{}".format(active),head=True)
        Git(self.path).checkout(bra) #如果说你的本地没有此分支的话，则必须要checkout
        return [{"id":c.hexsha,"message":c.message} for c in Repo(self.path).iter_commits()]

    def get_tags(self):
        return [str(tag) for tag in Repo(self.path).tags]


    def checkout(self,commit,bra,type):
        print(bra)
        """
        如果说是基于tag更新的话，则只需要checkout到对应的tag即可
        如果说是基于分支+提交记录的话，则需要先checkout到对应的分支，然后在reset到对应的提交记录
        :param commit:
        :param bra:
        :param type:
        :return:
        """
        Git(self.path).checkout(bra)
        if type=="bra":
            Repo(self.path).index.reset(commit=commit,head=True)

