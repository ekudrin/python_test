from pages.alerts_frame_windows_page import BrowserWindowPage, AlertsPage, FramesPage, NestedFramesPage, ModalDialogPage


class TestAlertsFrameWindow:
    class TestBrowserWindows:
        def test_new_tab(self, driver):
            browser_windows_page = BrowserWindowPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_tab()
            assert text_result == 'This is a sample page'

        def test_new_window(self, driver):
            browser_windows_page = BrowserWindowPage(driver, 'https://demoqa.com/browser-windows')
            browser_windows_page.open()
            text_result = browser_windows_page.check_opened_new_window()
            assert text_result == 'This is a sample page'

    class TestAlertsPage:
        def test_see_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_see_alert()
            assert alert_text == 'You clicked a button'

        def test_alert_appear_5_sec(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_alert_appear_5_sec()
            assert alert_text == 'This alert appeared after 5 seconds'

        def test_confirm_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            alert_text = alert_page.check_confirm_alert()
            assert alert_text == 'You selected Ok'

        def test_prompt_alert(self, driver):
            alert_page = AlertsPage(driver, 'https://demoqa.com/alerts')
            alert_page.open()
            text, text_result = alert_page.check_prompt_alert()
            assert 'You entered ' + text == text_result

    class TestFramesPage:

        def test_frames(self, driver):
            frame_page = FramesPage(driver, 'https://demoqa.com/frames')
            frame_page.open()
            result_frame1 = frame_page.check_frame('frame1')
            result_frame2 = frame_page.check_frame('frame2')
            assert result_frame1 == ['500px', '350px', 'This is a sample page']
            assert result_frame2 == ['100px', '100px', 'This is a sample page']

    class TestNestedFramesPage:

        def test_nested_frames(self, driver):
            nested_frame_page = NestedFramesPage(driver, 'https://demoqa.com/nestedframes')
            nested_frame_page.open()
            parent_text, child_text = nested_frame_page.check_nested_frame()
            assert parent_text == 'Parent frame'
            assert child_text == 'Child Iframe'

    class TestModalDialogsPage:

        def test_modal_dialogs(self, driver):
            modal_dialog_page = ModalDialogPage(driver, 'https://demoqa.com/modal-dialogs')
            modal_dialog_page.open()
            small, large = modal_dialog_page.check_modal_dialogs()
            assert small[0] == 'Small Modal'
            assert large[0] == 'Large Modal'
