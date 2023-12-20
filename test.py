import github_email
import os
os.environ['http_proxy'] = 'http://127.0.0.1:10809'  # 这里设置自己的代理端口号
os.environ['https_proxy'] = 'http://127.0.0.1:10809'  # 这里设置自己的代理端口号
github_api_auth = ('7f4f1e9922180be6017f', '56d6a38aa5f18147ea00d63f512bf4dbe6e160da')
# ges = github_email.collect_email_info('XingYu-Zhong', 'OpenAIAnyWhere', ['star'],github_api_auth=github_api_auth,request_limit=10)
ges = github_email.collect_email_info('Significant-Gravitas', 'AutoGPT', ['star'],github_api_auth=github_api_auth,request_limit=5)
result_list = {}
for ge in ges:
    if ge.email:
        result_list[ge.name] = ge.email

print(result_list)