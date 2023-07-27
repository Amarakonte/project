import { Component, OnInit } from '@angular/core';
import { PRODUCTS } from '../../datas';
import { Product } from '../../models/product';

@Component({
  selector: 'app-content-all-products',
  templateUrl: './content-all-products.component.html',
  styleUrls: ['./content-all-products.component.scss'],
})
export class ContentAllProductsComponent implements OnInit {
  public products?: Product[] = PRODUCTS;

  constructor() {}

  ngOnInit(): void {}
}
