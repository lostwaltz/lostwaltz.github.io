import os

filepath = 'site/index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Verify the file is fine
if '<div class="post-list">' in content:
    new_post = '''
    <a href="/posts/dependency-injection-in-unity/" class="post-item">
      <div class="post-meta">
        <span class="post-date">2026.03.06</span>
        <span class="tag">unity</span>
        <span class="tag">architecture</span>
        <span class="tag">devlog</span>
        <span class="tag">di</span>
      </div>
      <div class="post-title">유니티(Unity) 의존성 주입(DI)으로 싱글톤의 한계 극복하기</div>
      <div class="post-desc">오픈소스 프로젝트(Mate-Engine)의 스파게티 코드를 반면교사 삼아, 싱글톤 패턴의 한계를 극복하는 DI 아키텍처 도입기.</div>
    </a>
'''
    if 'dependency-injection-in-unity' not in content:
        content = content.replace('<div class="post-list">', '<div class="post-list">' + new_post)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print("Successfully updated index.html")
    else:
        print("Post already exists")
else:
    print("Could not find post-list div")
