const path = require('path');

const HtmlWebpackPlugin = require('html-webpack-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const ManifestPlugin = require('webpack-manifest-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

// Plugins
let plugins = [
  // Clean dist directory on build
  new CleanWebpackPlugin(),
  // Create manifest file
  new ManifestPlugin(),
  new MiniCssExtractPlugin({
    filename: '[name].css',
    chunkFilename: '[id].css',
    ignoreOrder: false,
  }),
  new HtmlWebpackPlugin({
    filename: 'about.html',
    template: './src/page_about.html',
  }),
  new HtmlWebpackPlugin({
    filename: 'index.html',
    template: './src/page_index.html',
  }),
]

// Rules
let rules = [
  {
    test: /\.s[ac]ss$/i,
    use: [
      // 'style-loader',
      {
      loader: MiniCssExtractPlugin.loader,
      options: {},
      },
      { loader: 'css-loader', options: { importLoaders: 1 } },
      'postcss-loader',
      'sass-loader',
    ],
  },
  {
    test: /\.(png|svg|jpe?g|gif)$/i,
    use: [
      'file-loader?name=./images/[name].[ext]',
    ],
  },
  {
    test: /\.(woff|woff2|eot|ttf|otf)$/i,
    use: [
      'file-loader?name=./fonts/[name].[ext]',
    ],
  },
]

module.exports = {
  mode: 'production', // production / development
  // https://webpack.js.org/configuration/devtool/
  devtool: undefined, //'inline-source-map',
  devServer: {
    contentBase: path.resolve(__dirname, 'dist'),
  },
  externals: {
    jquery: 'jQuery'
  },
  resolve: {
    alias: {
      NodeModules: path.resolve(__dirname, 'node_modules'),
    }
  },
  entry: {
    app: './src/app.js',
    // print: './src/app2.js'
  },
  output: {
    filename: '[name].bundle.js',
    path: path.resolve(__dirname, 'dist'),
    // publicPath: 'public/',
  },
  plugins: plugins,
  module: {
    rules: rules,
  },
  // optimization: {
  //   splitChunks: {
  //     chunks: 'all',
  //   },
  // },
};
