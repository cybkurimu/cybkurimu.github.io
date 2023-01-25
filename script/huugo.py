import fire
import server
import article
import content

class Huugo(object):
    """
    huugo [OPTION] [ACTION]
    
    [OPTION]:
        server --help                  status, start, stop, restart
        content --help                 Deal with the content of the article
        article --help                 about article attachment
        newposts [article-name]        Add new posts
    """
    def __init__(self, option, action):
        self.option = option
        self.action = action
    
    def server(action):
        """
        服务相关主控函数 server
        
        ACTIONS:
            status      View hugo server status
            start       Stat the hugo server
            stop        Stop the hugo server
            restart     Restart the hugo server
            
        Example: huugo server [status | start | stop | restart]
        """
        server.services(action)
                
    def content(action):
        """
        内容处理主控函数 content
        
        Example: huugo content add_pic_prefix      为图片添加 / 前缀
        """
        content.contents(action)

    def article(action):
        """
        文章处理主函数 article
        
        Example: huugo article del_empty_assets_folder     删除空的资产文件夹
        """
        article.articles(action)

    def newposts(article_name):
        """
        新建文章主函数 newposts, 不需要 .md 后缀
        
        Example: huugo newposts HelloWorld
        """
        article.newposts(article_name)

if __name__ == '__main__':
    fire.Fire(Huugo)
