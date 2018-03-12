const webpack = require('webpack');
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const merge = require('webpack-merge');
const webpackBaseConfig = require('./webpack.base.config.js');
const fs = require('fs');
fs.open('./build/env.js', 'w', (err, fd) => {
    const buf = 'export default "development";';
    fs.write(fd, buf, 0, buf.length, 0, (err, written, buffer) =>{});
});

function resolve (dir) {
    return path.join(__dirname, dir);
}

module.exports = merge(webpackBaseConfig, {
    devtool: '#source-map',
    output: {
        publicPath: '/dist/',
        filename: '[name].js',
        chunkFilename: '[name].chunk.js'
    },
    plugins: [
        new ExtractTextPlugin({
            filename: '[name].css',
            allChunks: true
        }),
        new webpack.optimize.CommonsChunkPlugin({
            name: 'vendors',
            filename: 'vendors.js'
        }),
        new HtmlWebpackPlugin({
            filename: '../index.html',
            template: './src/template/index.ejs',
            inject: false
        }),
        new webpack.optimize.ModuleConcatenationPlugin()
    ],
    /*本地开发环境*/
    devServer: {
        port:10086,
        proxy: {
            '/api/*': {
                target: 'http://localhost:8000',
                changeOrigin: true
            }
        }
    },
});