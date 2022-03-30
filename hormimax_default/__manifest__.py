# -----------------------------------------------------------------------------------
#
#    Copyright (C) 2021  Leonardo Bozzi  (http://www.vangrow.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------------
{
    'name': 'hormimax',
    'version': '13.0.1.0.0',
    'license': 'Other OSI approved licence',
    'category': 'Tools',
    'summary': 'Customización Hormimax',
    'author': 'Leonardo Bozzi',
    'depends': [
        # Applicaciones del Cliente
        'sale',
        'sale_management',
        'sale_order_type',
        'sale_order_type_ux',
        'purchase',
        'stock',
        'hr',
        'hr_expense',
        'note',
        'board',
        'calendar',
        'website',
        'crm',
        'sale_crm_ux',
        'crm_stage_teams',
        'base_ux',
        'stock_ux',
        'payroll',
        'mrp',

        # Contabilidad
        'account',
        'account_ux',
        'account_check',
        'account_financial_report',
        'account_journal_lock_date',
        'account_menu',
        'partner_statement',
        'account_journal_security',
        'account_netting',
        # 'om_account_accountant',
        # 'accounting_pdf_reports',
        'product_price_taxes_included',
        'sale_last_price_info',
        'purchase_last_price_info',
        # 'account_lock',
        'account_lock_date_update',
        'account_lock_to_date',
        'purchase_requisition',
        'purchase_requisition_stock',
        'purchase_ux',
        'account_statement_aeroo_report',
        'account_bank_statement_clear_partner',
        'account_bank_statement_import',
        'account_statement_move_import',
        'account_bank_statement_import_move_line',
        'account_bank_statement_import_transfer_move',
        'account_bank_statement_import_txt_xlsx',
        'account_cash_invoice',
        'sale_ux',
        'account_transfer_unreconcile',

        # Cybrosys
        'base_accounting_kit',
        'crm_kit',

        # Localización
        # All
        'l10n_ar',
        'l10n_ar_bank',
        'l10n_ar_account_withholding',
        'l10n_ar_sale',
        'l10n_ar_stock',
        'padron_afip',
        'report_qweb_pdf_watermark',

        # CE
        'l10n_ar_ux',
        'l10n_ar_afipws',
        'l10n_ar_afipws_fe',
        'l10n_ar_sale_order_type',
        'l10n_latam_invoice_document',
        'l10n_ar_reports',
        'l10n_ar_aeroo_base',

        # HR
        'hr_timesheet',
        # 'hr_timesheet_sheet',
        # 'hr_timesheet_activity_begin_end',
        'hr_timesheet_analysis',
        'hr_timesheet_attendance',
        'hr_timesheet_attendance_ux',
        'sale_timesheet_ux',
        'payroll_account',

        # MRP
        'mrp_bom_component_menu',
        'mrp_bom_current_stock',
        'mrp_bom_line_sequence',
        'mrp_bom_structure_report_level_1',
        'mrp_bom_structure_xlsx',
        'mrp_bom_structure_xlsx_level_1',
        'mrp_production_grouped_by_product',
        'mrp_production_note',
        'mrp_production_request',
        'mrp_workorder_sequence',

        # Custom
        'bit_timesheet_custom',
        'bit_attendance_custom',

        # Utils
        'web_search_with_and',
        'web_advanced_search',
        'auto_backup',
        'mass_editing',
        'intero_reload_form',
        'web_company_color',
        'backend_theme_v13',
        'odoo_whatsapp_integration',
        'mis_builder',
        'mis_builder_cash_flow',
        'mis_builder_demo',


    ],
    'data': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    'env-ver': '2',
    'odoo-license': 'CE',
    'port': '8069',
    # 'server_user': ''

    'config': [
        # 'addons_path' is always computed looking for the repositories in sources
        # 'data_dir' is a fixed location inside docker odoo image

        # You should use 2 worker threads + 1 cron thread per available CPU,
        # and 1 CPU per 10 concurent users.
        # if ommited oe will calculate workers and cron´s based on # of cpu
            'workers = 4',
            'max_cron_threads = 1',

        # Number of requests a worker will process before being recycled and
        # restarted. Defaults to 8192 if ommited
            'limit_request = 8192',

        # Maximum allowed virtual memory per worker. If the limit is exceeded,
        # the worker is killed and recycled at the end of the current request.
        # Defaults to 640MB
            'limit_memory_soft = 2147483648',

        # Hard limit on virtual memory, any worker exceeding the limit will be
        # immediately killed without waiting for the end of the current request
        # processing. Defaults to 768MB.
            'limit_memory_hard = 2684354560',
        # Prevents the worker from using more than CPU seconds for each request.
        # If the limit is exceeded, the worker is killed. Defaults to 60 sec.
            'limit_time_cpu = 1200',

        # Prevents the worker from taking longer than seconds to process a request.
        # If the limit is exceeded, the worker is killed. Defaults to 120. Differs
        # from --limit-time-cpu in that this is a "wall time" limit including e.g.
        # SQL queries.
            'limit_time_real = 2400',

        # default CSV separator for import and export
            'csv_internal_sep = ,',

        # disable loading demo data for modules to be installed
            'without_demo = False',

        # Comma-separated list of server-wide modules, there are modules loaded
        # automatically even if you do not create any database.
            'server_wide_modules = base,web,dbfilter_from_header',

        # Filter listed database REGEXP
            'dbfilter =',

            'db_maxconn = 64',
            'db_name = False',
            'db_password = odoo',
            'db_port = 5432',
            'db_sslmode = prefer',
            'db_template = template0',
            'db_user = odoo',
            'demo = {}',
            'email_from = False',
            'geoip_database = /usr/share/GeoIP/GeoLite2-City.mmdb',
            'http_enable = True',
            'http_interface =',
            'http_port = 8069',
            'limit_time_real_cron = -1',
            'list_db = True',
            'log_db = False',
            'log_db_level = warning',
            'log_handler = :INFO',
            'log_level = info',
            'logfile = /var/log/odoo/odoo.log',
            'osv_memory_age_limit = 1.0',
            'osv_memory_count_limit = False',
            'pg_path =',

            'proxy_mode = True',
            'reportgz = False',
            'screencasts =',
            'screenshots = /tmp/odoo_tests',
            'smtp_password = False',
            'smtp_port = 25',
            'smtp_server = localhost',
            'smtp_ssl = False',
            'smtp_user = False',
            'syslog = False',
            'test_enable = False',
            'test_file =',
            'test_tags = None',
            "translate_modules = ['all']",
            'unaccent = False',
            'upgrade_path =',
    ],

    'git-repos': [
        'https://github.com/leobozzi/cl-hormimax.git',
        'https://github.com/leobozzi/odoo-addons-utils bit-odoo-addons-utils',
        'https://github.com/leobozzi/odoo-custom bit-odoo-custom',


        # Odoomates
        # ==========================================================================================
        # 'https://github.com/odoomates/odooapps odoomates-odooapps',

        # CybtoAddons
        # ==========================================================================================
        'https://github.com/CybroOdoo/CybroAddons cybro-addons',

        # Gabriela Rivero
        # ==========================================================================================
        'https://github.com/regaby/odoo-custom regaby-odoo-custom',

        # OCA
        # ==========================================================================================
        # 'https://github.com/OCA/account-closing oca-account-closing',
        'https://github.com/OCA/account-financial-reporting oca-account-financial-reporting',  # noqa
        'https://github.com/OCA/account-financial-tools oca-account-financial-tools',
        'https://github.com/OCA/account-payment oca-account-payment',
        # 'https://github.com/OCA/apps-store oca-apps-store',
        'https://github.com/OCA/bank-payment oca-bank-payment',
        'https://github.com/OCA/bank-statement-import oca-bank-statement-import',
        'https://github.com/OCA/brand oca-brand',
        # 'https://github.com/OCA/business-requirement oca-business-requirement',
        # 'https://github.com/OCA/commission oca-commission',
        # 'https://github.com/OCA/contract oca-contract',
        # 'https://github.com/OCA/credit-control oca-credit-control',
        'https://github.com/OCA/crm oca-crm',
        # 'https://github.com/OCA/currency oca-currency',
        # 'https://github.com/OCA/ddmrp oca-ddmrp',
        # 'https://github.com/OCA/delivery-carrier oca-delivery-carrier',
        # 'https://github.com/OCA/e-commerce oca-e-commerce',
        # 'https://github.com/OCA/event oca-event',
        'https://github.com/OCA/field-service oca-field-service',
        'https://github.com/OCA/geospatial oca-geospatial',
        # 'https://github.com/OCA/helpdesk oca-helpdesk',
        'https://github.com/OCA/hr oca-hr',
        'https://github.com/OCA/hr-attendance oca-hr-attendance',
        'https://github.com/OCA/hr-holidays oca-hr-holidays',
        'https://github.com/OCA/hr-timesheet oca-hr-timesheet',
        # 'https://github.com/OCA/knowledge oca-knowledge',
        'https://github.com/OCA/stock-logistics-warehouse oca-stock-logistics-warehouse'
        # 'https://github.com/OCA/management-system oca-management-system',
        'https://github.com/OCA/manufacture oca-manufacture',
        'https://github.com/OCA/manufacture-reporting oca-manufacture-reporting',
        'https://github.com/OCA/margin-analysis oca-margin-analysis',
        'https://github.com/OCA/mis-builder oca-mis-builder',
        # 'https://github.com/OCA/multi-company oca-multi-company',
        # 'https://github.com/OCA/oca-custom oca-oca-custom',
        # 'https://github.com/OCA/operating-unit oca-operating-unit',
        'https://github.com/OCA/payroll.git oca-payroll',
        # 'https://github.com/OCA/partner-contact oca-partner-contact',
        # 'https://github.com/OCA/pos oca-pos',
        # 'https://github.com/OCA/product-attribute oca-product-attribute',
        # 'https://github.com/OCA/product-pack oca-product-pack',
        # 'https://github.com/OCA/project oca-project',
        # 'https://github.com/OCA/project-reporting oca-project-reporting',
        'https://github.com/OCA/purchase-workflow oca-purchase-workflow',
        # 'https://github.com/OCA/queue oca-queue',
        # 'https://github.com/OCA/report-print-send oca-report-print-send',
        'https://github.com/OCA/reporting-engine oca-reporting-engine',
        # 'https://github.com/OCA/sale-reporting oca-sale-reporting',
        'https://github.com/OCA/sale-workflow oca-sale-workflow',
        # 'https://github.com/OCA/server-auth oca-server-auth',
        # 'https://github.com/OCA/server-backend oca-server-backend',
        'https://github.com/OCA/server-tools oca-server-tools',
        'https://github.com/OCA/server-ux oca-server-ux',
        # 'https://github.com/OCA/social oca-social',
        'https://github.com/OCA/stock-logistics-barcode oca-stock-logistics-barcode',
        'https://github.com/OCA/stock-logistics-reporting oca-stock-logistics-reporting',
        'https://github.com/OCA/stock-logistics-transport oca-stock-logistics-transport',
        'https://github.com/OCA/stock-logistics-warehouse oca-stock-logistics-warehouse',
        'https://github.com/OCA/stock-logistics-workflow oca-stock-logistics-workflow',
        'https://github.com/OCA/timesheet oca-timesheet',
        # 'https://github.com/OCA/vertical-association oca-vertical-association',
        'https://github.com/OCA/web oca-web',
        # 'https://github.com/OCA/website oca-website',
        # 'https://github.com/OCA/account-analytic',

        # ADHOC
        # ==========================================================================================
        # 'https://github.com/ingadhoc/account-analytic ingadhoc-account-analytic',
        'https://github.com/ingadhoc/account-financial-tools ingadhoc-account-financial-tools',  # noqa
        'https://github.com/ingadhoc/account-payment ingadhoc-account-payment',
        'https://github.com/ingadhoc/aeroo_reports ingadhoc-aeroo_reports',
        'https://github.com/ingadhoc/argentina-reporting ingadhoc-argentina-reporting',
        'https://github.com/ingadhoc/argentina-sale ingadhoc-argentina-sale',
        'https://github.com/ingadhoc/hr ingadhoc-hr',
        'https://github.com/ingadhoc/miscellaneous ingadhoc-miscellaneous',
        # 'https://github.com/ingadhoc/multi-company ingadhoc-multi-company',
        # 'https://github.com/ingadhoc/multi-store ingadhoc-multi-store',

        # Fix porque falla la instalacion de l10n_ar_ux
        'https://github.com/ingadhoc/odoo-argentina ingadhoc-odoo-argentina',

        'https://github.com/ingadhoc/odoo-argentina-ce ingadhoc-odoo-argentina-ce',
        # 'https://github.com/ingadhoc/odoo-argentina-ee ingadhoc-odoo-argentina-ee',
        # 'https://github.com/ingadhoc/partner ingadhoc-partner',
        'https://github.com/ingadhoc/product ingadhoc-product',
        # 'https://github.com/ingadhoc/project ingadhoc-project',
        'https://github.com/ingadhoc/purchase ingadhoc-purchase',
        'https://github.com/ingadhoc/reporting-engine ingadhoc-reporting-engine',
        'https://github.com/ingadhoc/sale ingadhoc-sale',
        'https://github.com/ingadhoc/stock ingadhoc-stock',
        # 'https://github.com/ingadhoc/website ingadhoc-website',
    ],
    'docker-images': [
       #'odoo jobiols/odoo-jeo:13.0',
       'odoo lbozzi/odoo-docker-lb:13.0',
       'postgres postgres:11.1-alpine',
       'aeroo adhoc/aeroo-docs',
       'nginx nginx',
    ]
}
