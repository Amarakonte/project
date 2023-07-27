import { Component, Input, OnInit } from '@angular/core';
import { Product } from '../../models/product';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.scss'],
})
export class ProductItemComponent implements OnInit {
  @Input() public img!: string;
  @Input() public preview!: string[];
  @Input() public title!: string;
  @Input() public product!: Product;

  constructor() {}

  ngOnInit(): void {}
}
