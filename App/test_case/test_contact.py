from App.Page.app import App


class TestContact:

    def setup(self):
        self.app = App()
        self.main= self.app.start().goto_main()

    def test_addcontact(self):
        name = "hogwarts_010"
        gender = "男"
        phonenum = "13500000010"

        result = self.main.goto_address().\
            click_addmember().\
            add_member_menu().\
            add_contact(name, gender, phonenum).get_toast()
        assert "添加成功" == result