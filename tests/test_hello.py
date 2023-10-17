import pytest
from ptest import hello


def test_print(capsys):
    hello()

    captured = capsys.readouterr()
    assert captured.out == "hello\n"


@pytest.mark.parametrize(
    "static_data, date_timestamp, date_string, expect_html",
    [
        # test-data [demo]
        (
            [
                {
                    "captured_image_path": "./static/cache/form/Presidential_Biden_02.jpg",
                    "sample_image_path": "./static/cache/formPresidential_Biden_01.jpg",
                    "id": "00059",
                    "name": "拜登",
                },
                {
                    "captured_image_path": "./static/cache/formPresidential_Trump_02.jpg",
                    "sample_image_path": "./static/cache/formPresidential_Biden_01.jpg",
                    "id": "00059",
                    "name": "拜登",
                },
                {
                    "captured_image_path": "./static/cache/formPresidential_Biden_03.jpg",
                    "sample_image_path": "./static/cache/formPresidential_Biden_01.jpg",
                    "id": "00059",
                    "name": "拜登",
                },
            ],
            "1697040000",
            "2023-10-12",
            '<!doctype html>\n<html lang="en">\n  <head>\n    <meta charset="UTF-8" />\n    <meta name="viewport" content="width=device-width, initial-scale=1.0" />\n    <title>人工審查系統</title>\n    <link\n      rel="stylesheet"\n      href="/static//css/mrs.css"\n    />\n    <link\n      rel=" shortcut icon"\n      href="/static//images/favicon.ico"\n    />\n  </head>\n  <body>\n    <header>\n      <h1>臉部辨識人工審查系統</h1>\n    </header>\n\n    <form action="/mr" method="POST">\n      <table class="mrs-table" border="1">\n        <tr>\n          <th colspan="2">臉部抓取影像是否為該員工</th>\n          <th rowspan="2">臉部抓取影像</th>\n          <th colspan="3">被辨識為該員工</th>\n        </tr>\n        <tr>\n          <th>是</th>\n          <th>否/不確定</th>\n          <th>員工照</th>\n          <th>員工編號</th>\n          <th>員工姓名</th>\n        </tr>\n        \n        <tr>\n          <td class="yes-cell">\n            <label>\n              <input\n                type="radio"\n                name="answer_./static/cache/form/Presidential_Biden_02.jpg"\n                value="00059_yes"\n              />\n            </label>\n          </td>\n          <td class="no-cell">\n            <label>\n              <input\n                type="radio"\n                name="answer_./static/cache/form/Presidential_Biden_02.jpg"\n                value="00059_no"\n              />\n            </label>\n          </td>\n          <td>\n            <img src="./static/cache/form/Presidential_Biden_02.jpg" alt="picture" />\n            <!-- ./static/cache/form/Presidential_Biden_02.jpg -->\n          </td>\n          <td>\n            <img src="./static/cache/formPresidential_Biden_01.jpg" alt="picture" />\n            <!-- ./static/cache/formPresidential_Biden_01.jpg -->\n          </td>\n          <td>00059</td>\n          <td>拜登</td>\n        </tr>\n        \n        <tr>\n          <td class="yes-cell">\n            <label>\n              <input\n                type="radio"\n                name="answer_./static/cache/formPresidential_Trump_02.jpg"\n                value="00059_yes"\n              />\n            </label>\n          </td>\n          <td class="no-cell">\n            <label>\n              <input\n                type="radio"\n                name="answer_./static/cache/formPresidential_Trump_02.jpg"\n                value="00059_no"\n              />\n            </label>\n          </td>\n          <td>\n            <img src="./static/cache/formPresidential_Trump_02.jpg" alt="picture" />\n            <!-- ./static/cache/formPresidential_Trump_02.jpg -->\n          </td>\n          <td>\n            <img src="./static/cache/formPresidential_Biden_01.jpg" alt="picture" />\n            <!-- ./static/cache/formPresidential_Biden_01.jpg -->\n          </td>\n          <td>00059</td>\n          <td>拜登</td>\n        </tr>\n        \n        <tr>\n          <td class="yes-cell">\n            <label>\n              <input\n                type="radio"\n                name="answer_./static/cache/formPresidential_Biden_03.jpg"\n                value="00059_yes"\n              />\n            </label>\n          </td>\n          <td class="no-cell">\n            <label>\n              <input\n                type="radio"\n                name="answer_./static/cache/formPresidential_Biden_03.jpg"\n                value="00059_no"\n              />\n            </label>\n          </td>\n          <td>\n            <img src="./static/cache/formPresidential_Biden_03.jpg" alt="picture" />\n            <!-- ./static/cache/formPresidential_Biden_03.jpg -->\n          </td>\n          <td>\n            <img src="./static/cache/formPresidential_Biden_01.jpg" alt="picture" />\n            <!-- ./static/cache/formPresidential_Biden_01.jpg -->\n          </td>\n          <td>00059</td>\n          <td>拜登</td>\n        </tr>\n        \n      </table>\n      <input type="submit" value="提交答案" />\n    </form>\n  </body>\n</html>',
        ),
        # end-test-data
    ],
)
def test_flask_create_get(static_data, date_timestamp, date_string, expect_html):
    assert False
