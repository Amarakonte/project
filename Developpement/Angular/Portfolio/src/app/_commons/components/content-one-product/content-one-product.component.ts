import { Component, Input, OnInit } from '@angular/core';
import { Product } from '../../models/product';

@Component({
  selector: 'app-content-one-product',
  templateUrl: './content-one-product.component.html',
  styleUrls: ['./content-one-product.component.scss'],
})
export class ContentOneProductComponent implements OnInit {
  @Input() public product!: Product;

  constructor() {}

  public ngOnInit(): void {}
}
