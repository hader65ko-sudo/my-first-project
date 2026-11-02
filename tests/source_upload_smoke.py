from pathlib import Path
import os
from playwright.sync_api import sync_playwright,expect
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.goto(os.environ.get('APP_URL','http://127.0.0.1:5173'));page.get_by_role('button',name='المكتبة والمصادر',exact=True).click();expect(page.locator('.source-page').first).to_be_visible()
 page.locator('input[type=file]').set_input_files(str(Path(__file__).resolve().parent.parent/'public/chemistry-source.pdf'))
 expect(page.locator('.notice')).to_contain_text('تم فتح',timeout=120000)
 print(page.locator('.notice').inner_text());assert page.locator('.source-page').count()==119
 assert not errors,errors
 page.set_viewport_size({'width':390,'height':844});page.get_by_role('button',name='فتح القائمة').click();page.get_by_role('button',name='الرئيسية',exact=True).click();page.wait_for_timeout(800);page.screenshot(path='/tmp/chemistry-mobile-light.png',full_page=True)
 page.get_by_role('button',name='فتح القائمة').click();page.get_by_role('button',name='فصول المنهج',exact=True).click();page.wait_for_timeout(400)
 for i in range(7):
  page.locator('.chapter-card').nth(i).click();page.locator('.lesson-row').first.click();page.wait_for_timeout(500);expect(page.locator('.simulation')).to_be_visible();assert page.evaluate('document.documentElement.scrollWidth <= innerWidth');page.get_by_role('button',name='وضع الحفظ').click();page.locator('.flashcard').click();page.get_by_role('button',name='وضع الاختبار').click();expect(page.locator('.options button')).to_have_count(3);page.get_by_role('button',name='العودة إلى',exact=False).click();page.wait_for_timeout(500)
 print('PASS: PDF extraction, all 7 chapter workflows on mobile, no horizontal overflow; errors',errors)
 b.close()
