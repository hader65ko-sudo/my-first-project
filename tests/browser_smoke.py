import os
from playwright.sync_api import sync_playwright, expect
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'])
 page=b.new_page(viewport={'width':1440,'height':1100});errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto(os.environ.get('APP_URL','http://127.0.0.1:5173'));page.wait_for_timeout(1200);page.screenshot(path='/tmp/chemistry-home.png',full_page=True)
 assert page.get_by_role('heading',name='افهمها اليوم، تذكّرها دائماً.').is_visible()
 page.get_by_role('button',name='استكشف المختبر').click();expect(page.locator('.simulation')).to_be_visible()
 before=page.locator('.sim-result').inner_text();page.get_by_role('slider',name='الضغط',exact=True).fill('4');assert page.locator('.sim-result').inner_text()!=before
 page.get_by_role('button',name='وضع الحفظ').click();page.locator('.flashcard').click();page.wait_for_timeout(250);assert page.locator('.flashcard').inner_text().find('تتساوى')>=0
 page.get_by_role('button',name='وضع الاختبار').click();page.locator('.options button').nth(0).click();assert 'قريب' in page.locator('.feedback').inner_text()
 page.get_by_role('button',name='أعد المحاولة').click();page.locator('.options button').nth(1).click();assert 'أحسنت' in page.locator('.feedback').inner_text()
 page.reload();page.get_by_role('button',name='فصول المنهج',exact=True).click();expect(page.locator('.chapter-card').first).to_be_visible();assert '100٪' not in page.locator('.chapter-card').first.inner_text();assert '33٪' in page.locator('.chapter-card').nth(1).inner_text()
 page.get_by_role('button',name='الوضع الليلي').click();assert page.locator('html').get_attribute('data-theme')=='dark'
 page.get_by_role('button',name='المكتبة والمصادر',exact=True).click();expect(page.locator('.source-page').first).to_be_visible();assert page.locator('.source-page').count()>100
 page.get_by_placeholder('ابحث داخل النص المستخرج…').fill('الثرموداينمك');assert 0<page.locator('.source-page').count()<100
 page.get_by_role('button',name='افتح المصدر',exact=True).click();assert page.get_by_role('dialog').is_visible();page.get_by_role('button',name='إغلاق المصدر').click()
 page.set_viewport_size({'width':390,'height':844});page.get_by_role('button',name='فتح القائمة').click();page.get_by_role('button',name='الرئيسية',exact=True).click();expect(page.locator('.hero')).to_be_visible();page.wait_for_timeout(400);page.screenshot(path='/tmp/chemistry-mobile.png',full_page=True)
 assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
 print('PASS: dashboard, pressure simulation, flashcard, wrong/correct quiz, persisted progress, dark mode, source search, PDF viewer, mobile navigation; JS errors:',errors)
 assert not errors
 b.close()
