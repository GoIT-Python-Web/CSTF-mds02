# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BooksGraberPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        adapter['rating'] = adapter['rating'].replace('One', '1').replace('Two', '2').replace('Three', '3').replace(
            'Four', '4').replace('Five', '5')
        return item
