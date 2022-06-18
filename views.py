"""
This module is used to output `Clockify.me` data.
"""
from typing import Iterable

import xlsxwriter as xlsxwriter


def print_list_elements(elements: Iterable) -> None:
    for element in elements:
        print(element)


def show_error_message(message: str) -> None:
    print(message)


class ExcelReporter:
    """Report to `Excel` file."""
    def __init__(self, name: str):
        self._name = name
        self.main_format = {
                'align': 'center',
                'valign': 'vcenter',
                'font_size': 14
            }

    @staticmethod
    def _create_worksheet_with_headers(
            workbook, name: str, formatter: str,
            headers_names: tuple[str, str, str]
    ):
        """Create `worksheet` with 3 needed headers."""
        worksheet = workbook.add_worksheet(name)

        worksheet.write('A1', headers_names[0], formatter)
        worksheet.write('B1', headers_names[1], formatter)
        worksheet.write('C1', headers_names[2], formatter)

        return worksheet

    def _create_all_info_report_worksheet(
            self, workbook, header_formatter,
            center_formatter, wrap_formatter,
            all_info_report: list[dict]
    ) -> None:
        """
        Create `worksheet` with all info about tasks.
        Needed for task 8, part 1.
        """
        worksheet = self._create_worksheet_with_headers(
            workbook, "Full report", header_formatter,
            ("name", "description", "duration")
        )

        worksheet.set_column(1, 2, 20)
        worksheet.set_column(0, 0, 50)

        row = 1
        col = 0

        for _ in all_info_report:
            worksheet.write(row, col, _['name'], wrap_formatter)
            worksheet.write(row, col + 1, _['description'], center_formatter)
            worksheet.write(row, col + 2, _['duration'], center_formatter)
            row += 1

    def _create_grouped_by_dates_report_worksheet(
            self, workbook, header_formatter,
            center_formatter, wrap_formatter,
            grouped_by_date_report: list[dict]
    ) -> None:
        """
        Create `worksheet` with tasks grouped by dates.
        Needed for task 8, part 2.
        """
        worksheet = self._create_worksheet_with_headers(
            workbook, "Grouped by dates report", header_formatter,
            ("date", "name", "duration")
        )

        worksheet.set_column(0, 0, 20)
        worksheet.set_column(1, 1, 50)
        worksheet.set_column(2, 2, 20)

        row = 1
        col = 0

        for date_group in grouped_by_date_report:
            date = list(date_group.keys())[0]
            group = date_group[date]

            worksheet.merge_range(
                row, 0, len(group), 0, date, center_formatter)
            for item in group:
                worksheet.write(row, col + 1, item['name'], wrap_formatter)
                worksheet.write(
                    row, col + 2, item['duration'], center_formatter)
                row += 1

    def create_formatters(self, workbook) -> tuple:
        """
        Create formatters to display
        special styles in `Excel` file.
        """
        header_formatter = workbook.add_format(
            self.main_format | {'bold': True})
        center_formatter = workbook.add_format(self.main_format)

        wrap_format = self.main_format.copy()
        wrap_format.pop("align")
        wrap_formatter = workbook.add_format(wrap_format | {'text_wrap': True})

        return header_formatter, center_formatter, wrap_formatter

    def create_report_file(
            self, all_info_report: list[dict],
            grouped_by_date_report: list[dict]
    ) -> None:
        """Create final report `Excel` file."""
        with xlsxwriter.Workbook(self._name) as workbook:
            header_formatter, center_formatter, wrap_formatter = \
                self.create_formatters(workbook)

            self._create_all_info_report_worksheet(
                workbook, header_formatter, center_formatter,
                wrap_formatter, all_info_report
            )

            self._create_grouped_by_dates_report_worksheet(
                workbook, header_formatter, center_formatter,
                wrap_formatter, grouped_by_date_report
            )
